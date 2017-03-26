#!/usr/bin/perl -w

################################################################################
#
# File:        		emma_instrument_codecenter.pl
# Description:    	Instrument CodeCenter .jar files
# Author:        	Qian Ouyang
# Created:        	Tue Jan 8, 2008
# License:         	All rights reserved by Black Duck Software, 2008.
#
################################################################################


################################################################################
#                    Modules                            #
################################################################################

$|++;
use strict;
use English;
use Getopt::Long;
   $Getopt::Long::autoabbrev = 1;
   $Getopt::Long::ignorecase = 0;

################################################################################
#            Constant Variables and Variables                    #
################################################################################

use constant CHK_SLP => 10;
my $CODECENTER_HOME= "/opt/blackduck/CodeCenter";
my $QIAN_SANDBOX= "/home/qian_emma/coverage";
my $MAILTO= "qouyang\@blackducksoftware.com";
my $UNZIP_ROOT_WAR= "/tmp/qian/unzip_root_war";
my $JAR_LOCATION= "/mnt/qa/qian/jdk-6u3-linux/jdk1.6.0_03/bin";
my $EMMA_HOME= "$CODECENTER_HOME/lib/jre/lib/ext";
my $jars;
my @jars;
my $cmd = "";


my $current_date;
my $commandline_option;
my $system_call;
my $help = "";
my $output = "";


my $help_string = <<HELP;
Instrument emma tool on 10.12.13.165 for CodeCenter. The Emma build is 2.1.5320.

Usage:  perl emma_instrument_codecenter.pl

1). stop tomcat
2). remove old .em files
3). unzip ROOT.war
4). instrument .jars and mv coverage.em
5). repack ROOT.war and replace the original ROOT.war
6). re-start tomcat
7). merge coverage.em files
8). send email
HELP

################################################################################
#                        Main                            #
################################################################################

get_input();

`/etc/init.d/bds-codecenter-tomcat stop`;
print "stopped tomcat\n"; 
sleep(CHK_SLP);
`rm -rf /$CODECENTER_HOME/tomcat/webapps/ROOT`;
print "removed ROOT folder\n";

#remove old em files
chdir "/tmp/qian";
`rm -rf em_file`;
mkdir "em_file";
chdir $QIAN_SANDBOX;
`rm *.em`;
print "removed old .em files\n";


#clean content $UNZIP_ROOT_WAR and unzip ROOT.war
`rm -rf $UNZIP_ROOT_WAR`;
`mkdir -p $UNZIP_ROOT_WAR`;
print "removed old unzipped ROOT.war\n";
chdir "$CODECENTER_HOME/tomcat/webapps";
`unzip ROOT.war -d $UNZIP_ROOT_WAR`;
print "unzipped ROOT.war\n";

#instrument .jar 
chdir "$UNZIP_ROOT_WAR/WEB-INF/lib";

@jars = qw(bds-forum bds-modelbase catalogip-base catalogip catalogip-json catalogip-kb catalogip-util catalogip-vuln codecenter-regupdate);
my $i = 1;
foreach $jars(@jars) {
#$cmd = "java -cp $EMMA_HOME/emma.jar emma instr -m overwrite -ip $jars" . ".jar -ix -com.blackducksoftware.springtestng.*,-com.blackducksoftware.testng.*,-com.blackducksoftware.soap.axis.test.*,*.db.*";
$cmd = "java -cp $EMMA_HOME/emma.jar emma instr -m overwrite -ip $jars" . ".jar -ix -com.blackducksoftware.springtestng.* -ix -com.blackducksoftware.testng.* -ix -com.blackducksoftware.soap.axis.test.* -ix -org.json.*";
print $cmd;
$output = `$cmd 2>&1`;
print "$output";
$cmd = "mv coverage.em /tmp/qian/em_file/coverage$i" . ".em";
`$cmd`;
print "implemented $jars" . ".jar\n";
$i++;
}

#reconstitue ROOT.war and replace original ROOT.war
chdir $UNZIP_ROOT_WAR;
`$JAR_LOCATION/jar -cvf ROOT.war .`;
print "repacked ROOT.war\n";
`rm /$CODECENTER_HOME/tomcat/webapps/ROOT.war`;
print "removed original ROOT.war\n";
`cp ROOT.war $CODECENTER_HOME/tomcat/webapps`;
print "placed implemented ROOT.war\n";
`chmod 777 $CODECENTER_HOME/tomcat/webapps/ROOT.war`;
print "changed permission of ROOT.war\n";


#re-start tomcat
`/etc/init.d/bds-codecenter-tomcat start`;
print "started tomcat\n";

#merge all the .em files and cp to $QIAN_SANDBOX
chdir "/tmp/qian/em_file";
`java -cp $EMMA_HOME/emma.jar emma merge -in coverage1.em -in coverage2.em -in coverage3.em -in coverage4.em -in coverage5.em -in coverage6.em -in coverage7.em -in coverage8.em -in coverage9.em -in coverage10.em -out merged_coverage.em`;
`cp merged_coverage.em $QIAN_SANDBOX`;
print "merged .em files\n";


#send e-mail indicating instrumentation completed, this section is not quite right!
chdir $QIAN_SANDBOX;
$current_date = `date '+DATE_%m_%d_%y_TIME_%H-%M-%S'`;
`mail $MAILTO -s \"$current_date instrumentation complete on 10.12.13.165 for CodeCenter\" <emma.props`;
print "sent instrumentation complete message\n";


exit(0);


################################################################################
#                    Subroutine                            #
################################################################################
 
# Get commandline input and assign to variable.
sub get_input
{

    # Get options.
    $commandline_option = GetOptions("help" => \$help);

      die ("Please use --help for information.\nProgram exiting.\n") unless $commandline_option;



# If 'Help' option
      if ($help) {
        print $help_string;
      exit(1);
        }

  }

    exit (0);