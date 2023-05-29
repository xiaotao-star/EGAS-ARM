import java.io.File;

import de.jstacs.DataType;
import de.jstacs.io.FileManager;
import de.jstacs.parameters.ExpandableParameterSet;
import de.jstacs.parameters.Parameter;
import de.jstacs.parameters.ParameterSet;
import de.jstacs.parameters.ParameterSetContainer;
import de.jstacs.results.Result;
import de.jstacs.results.ResultSet;
import de.jstacs.results.TextResult;
import de.jstacs.results.savers.ResultSaver;
import de.jstacs.results.savers.ResultSaverLibrary;
import de.jstacs.tools.JstacsTool;
import de.jstacs.tools.ProgressUpdater;
import de.jstacs.tools.ToolParameterSet;
import de.jstacs.tools.ToolResult;
import de.jstacs.tools.ui.cli.CLI;
import de.jstacs.tools.ui.cli.CLI.QuietSysProtocol;
import de.jstacs.tools.ui.cli.CLI.SysProtocol;
import projects.gemoma.AddAttribute;
import projects.gemoma.AnnotationFinalizer;
import projects.gemoma.CheckIntrons;
import projects.gemoma.DenoiseIntrons;
import projects.gemoma.ExtractRNAseqEvidence;
import projects.gemoma.Extractor;
import projects.gemoma.GeMoMaAnnotationFilter;
import projects.gemoma.GeMoMaPipeline;
import projects.gemoma.Tools;
import projects.gemoma.GeMoMa;

public class TestCreator {

	static SysProtocol protocol = new QuietSysProtocol();
	static ProgressUpdater progress = new ProgressUpdater();
	
	public static void main(String[] args) throws Exception {
		File basic = new File(Tools.GeMoMa_TEMP);
		basic.mkdirs();
		
		switch( args[0] ) {
			case "create":
				//clear
				for(File file: new File("tests/gemoma/intermediate/").listFiles()) file.delete(); 

				create( new Extractor(100), 
						new String[][] {{"genome"}, {"annotation"}},
						new String[] {"tests/gemoma/ref-fragment.fasta", "tests/gemoma/ref-annotation.gff"},
						"tests/gemoma/", "extractor-test.xml"
				);
				
				create( new ExtractRNAseqEvidence(), 
						new String[][] {{"mapped reads","mapped reads no. 1", "mapped reads file"}, {"coverage"}},
						new String[] {"tests/gemoma/target-accepted_hits.bam", "true"},
						"tests/gemoma/", "ere-test.xml"
				);
				
				create( new CheckIntrons(), 
						new String[][] {{"target genome"}, {"introns", "introns no. 1", "introns"} },
						new String[] {"tests/gemoma/target-fragment.fasta", "tests/gemoma/intermediate/introns.gff"},
						"tests/gemoma/", "checkintrons-test.xml"
				);
				
				create( new DenoiseIntrons(), 
						new String[][] {{"introns", "introns no. 1", "introns"}, {"coverage", "coverage no. 1"}, {"coverage", "coverage no. 1", "coverage", "coverage_unstranded"}},
						new String[] {"tests/gemoma/intermediate/introns.gff", "UNSTRANDED", "tests/gemoma/intermediate/coverage.bedgraph"},
						"tests/gemoma/", "denoise-test.xml"
				);/**/

				create( new GeMoMa(100,3600,604800),
						new String[][] {
							{"search results"},
							{"target genome"},
							{"cds parts"},
							{"assignment"},
							{"introns", "introns no. 1", "introns"},
							{"coverage", "coverage no. 1"},
							{"coverage", "coverage no. 1", "coverage", "coverage_unstranded"}
						},
						new String[] {
							"tests/gemoma/tblastn.txt",
							"tests/gemoma/target-fragment.fasta",
							"tests/gemoma/intermediate/cds-parts.fasta",
							"tests/gemoma/intermediate/assignment.tabular",
							"tests/gemoma/intermediate/denoised_introns.gff",
							"UNSTRANDED",
							"tests/gemoma/intermediate/coverage.bedgraph"
						},
						"tests/gemoma/", "gemoma-test.xml"
				);
				
				create( new GeMoMaAnnotationFilter(), 
						new String[][] {{"predicted annotation","gene annotations no. 1","gene annotation file"}},
						new String[] {"tests/gemoma/intermediate/predicted_annotation.gff"},
						"tests/gemoma/", "gaf-test.xml"
				);
				
				create( new AnnotationFinalizer(), 
						new String[][] { {"UTR"},{"annotation"}, {"genome"}, {"rename"}	},
						new String[] {"NO", "tests/gemoma/intermediate/filtered_predictions.gff", "tests/gemoma/target-fragment.fasta", "NO"},
						"tests/gemoma/", "af-test-nothing.xml"
				);
				
				create( new AnnotationFinalizer(), 
						new String[][] {
							{"UTR"},
							{"UTR", "introns", "introns no. 1", "introns file"},
							{"UTR", "coverage", "coverage no. 1"},
							{"UTR", "coverage", "coverage no. 1", "coverage file", "coverage_unstranded"},
							{"annotation"},
							{"genome"},
							{"rename"},
							{"rename", "prefix"},
							{"name attribute"}
						},
						new String[] {
							"YES",
							"tests/gemoma/intermediate/denoised_introns.gff",
							"UNSTRANDED",
							"tests/gemoma/intermediate/coverage.bedgraph",
							"tests/gemoma/intermediate/filtered_predictions.gff",
							"tests/gemoma/target-fragment.fasta",
							"SIMPLE",
							"abc",
							"false"
						},
						"tests/gemoma/", "af-test-utr.xml"
				);
				
				create( new GeMoMaPipeline(),
						new String[][] {
							{"target genome"}, 
							{"reference species", "reference no. 1", "species", "genome"}, 
							{"reference species", "reference no. 1", "species", "annotation"}, 
							{"RNA-seq evidence"},
							{"RNA-seq evidence", "mapped reads","mapped reads no. 1", "mapped reads file"}, 
							{"RNA-seq evidence", "coverage" },
							{"AnnotationFinalizer parameter set", "rename"},
							{"AnnotationFinalizer parameter set", "rename", "prefix"},
							{"AnnotationFinalizer parameter set", "name attribute"},
							{"output individual predictions"}
						},
						new String[] {
							"tests/gemoma/target-fragment.fasta",
							"tests/gemoma/ref-fragment.fasta",
							"tests/gemoma/ref-annotation.gff",
							"MAPPED",
							"tests/gemoma/target-accepted_hits.bam",
							"true",
							"SIMPLE",
							"abc",
							"false",
							"true"
						},
						"tests/gemoma/", "gemomapipeline-test.xml"
				);
				
				create( new GeMoMaPipeline(),
						new String[][] {
							{"target genome"}, 
							{"reference species", "reference no. 1", "species", "genome"}, 
							{"reference species", "reference no. 1", "species", "annotation"},
							{"selected"},
							{"tblastn"},
							{"RNA-seq evidence"},
							{"AnnotationFinalizer parameter set", "rename"}
						},
						new String[] {
							"tests/gemoma/target-fragment.fasta",
							"tests/gemoma/ref-fragment.fasta",
							"tests/gemoma/ref-annotation.gff",
							"tests/gemoma/selected.tabular",
							"true",
							"NO",
							"NO"
						},
						"tests/gemoma/", "gemomapipeline-test2.xml"
				);
				
				
				create( new GeMoMaPipeline(),
						new String[][] {
							{"target genome"}, 
							{"reference species", "reference no. 1", "species", "genome"}, 
							{"reference species", "reference no. 1", "species", "annotation"}, 
							{"RNA-seq evidence"},
							{"RNA-seq evidence", "Stranded"},
							{"RNA-seq evidence", "mapped reads","mapped reads no. 1", "mapped reads file"}, 
							{"RNA-seq evidence", "coverage" },
							{"AnnotationFinalizer parameter set", "UTR"},
							{"AnnotationFinalizer parameter set", "rename"},
							{"AnnotationFinalizer parameter set", "rename", "prefix"},
							{"AnnotationFinalizer parameter set", "name attribute"},
							{"synteny check"},
							{"output individual predictions"}
						},
						new String[] {
							"tests/gemoma/target-fragment.fasta",
							"tests/gemoma/ref-fragment.fasta",
							"tests/gemoma/ref-annotation.gff",
							"MAPPED",
							"FR_SECOND_STRAND",
							"tests/gemoma/target-accepted_hits.bam",
							"true",
							"YES",
							"SIMPLE",
							"abc",
							"false",
							"true",
							"true"
						},
						"tests/gemoma/", "gemomapipeline-test3.xml"
				);
				
				create( new AddAttribute(),
						new String[][] {
							{"annotation"}, 
							{"attribute"}, 
							{"table"}, 
							{"ID column"},
							{"type", "attribute column"},
						},
						new String[] {
							"tests/gemoma/intermediate/predicted_annotation.gff",
							"newAttribute",
							"tests/gemoma/additionalInfo.txt",
							"0",
							"1",
						},
						"tests/gemoma/", "addAttribute-test.xml"
				);

				create( new AddAttribute(),
						new String[][] {
							{"annotation"}, 
							{"attribute"}, 
							{"table"}, 
							{"ID column"},
							{"type"},
						},
						new String[] {
							"tests/gemoma/intermediate/predicted_annotation.gff",
							"isFavourite",
							"tests/gemoma/additionalInfo.txt",
							"0",
							"BINARY",
						},
						"tests/gemoma/", "addAttribute-test2.xml"
				);
				/**/
				break;
				
			case "test":
				boolean verbose=true;
				JstacsTool[] jt = {
						new ExtractRNAseqEvidence(),
						new Extractor(100),
						new DenoiseIntrons(),
						new GeMoMa(100,3600,604800),
						new GeMoMaAnnotationFilter(),
						new AnnotationFinalizer(),
						new GeMoMaPipeline(),
						new AddAttribute()
				};
				double all = 0;
				File jarfile = new File(CLI.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath());
				for( JstacsTool t: jt ) {
					double success=JstacsTool.test( t, jarfile.getParentFile().getAbsolutePath(), verbose );
					System.out.println( "test summary\t" + t.getShortName() + "\t" + success );
					all += success;
				}
				System.out.println( "\n\ntest summary\tPROBLEMS\t" + (jt.length-all) );
				break;
				
			default:
				System.out.println("unknown option: " + args[0] );
		}
	}
	
	public static void create(JstacsTool t, String[][] key, String[] value, String dir, String fName) throws Exception {
		protocol.append("create test case for " + t.getShortName() + "\n");
		
		//create parameters
		t.clear();
		ToolParameterSet p = t.getToolParameters();
		
		//set parameters
		for( int i = 0; i < key.length; i++ ) {
			Parameter q = null;
			ParameterSet ps = p;
			for( int j = 0; j < key[i].length; j++ ) {
				//System.out.println(key[i][j]);
				q = ps.getParameterForName(key[i][j]);
				if( ps instanceof ExpandableParameterSet && q==null ) {
					ExpandableParameterSet e = (ExpandableParameterSet) ps;
					e.addParameterToSet();
					q = ps.getParameterForName(key[i][j]);
				}
				/*
				if( q==null ) {
					System.out.println("PROBLEM " + ps.getParameterAt(0).getName());
				} else {
					System.out.println(q.getClass());
				}/**/
				
				if( q instanceof ParameterSetContainer ) {
					ps = ((ParameterSetContainer)q).getValue();
				} else if( q.getDatatype() == DataType.PARAMETERSET ) {
					ps = (ParameterSet) q.getValue();
				}
			}
			if( !q.checkValue(value[i]) && q.getDatatype()==DataType.PARAMETERSET ) {
				ps = (ParameterSet)q.getValue();
				q=ps.getParameterAt(0);
			}
			//System.out.println(Arrays.toString(key[i]) + "\t" + q.getName() + "\t" + q.getDatatype() + "\t" + value[i] );
			q.setValue(value[i]);
		}
		
		//run
		ToolResult tr = null;
		try {
			tr = t.run(p, protocol, progress, 1);
		} catch( Exception e ) {
			tr = t.run(p, new SysProtocol(), progress, 1);
		}
		
		//save
		if( tr != null) {
			ResultSaver saver = ResultSaverLibrary.getSaver( tr.getClass() );
			saver.writeOutput( tr, new File(dir+"intermediate/") );
			FileManager.writeFile(dir+"xml/"+fName, tr.toXML());
			System.out.println(t.getShortName() + ": results saved" );
		}
	}
	
	static void getContent( ResultSet rs ) {
		for( int i = 0; i < rs.getNumberOfResults(); i++ ) {
			Result r = rs.getResultAt(i);
			if( r instanceof TextResult ) {
				TextResult t = (TextResult) r;
				t.getValue().getContent();
			}
		}
	}
}
