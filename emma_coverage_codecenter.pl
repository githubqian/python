#!/usr/bin/perl -w

################################################################################
#
# File:		        emma_coverage_codecenter.pl
# Description:    	Get accumulative test coverage output in .html and .txt format
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


my $current_date;
my $commandline_option;
my $system_call;
my $help = "";


my $help_string = <<HELP;
Generate emma coverage report on 10.12.13.165 for CodeCenter. The % is accumulative, unless tomcat is shutdown and restarted manually, which will reset the coverage %.

Usage:  perl emma_coverage_codecenter.pl

The Emma build is 2.1.5320 which doesn't need to shutdown tomcat to get coverager.ec file. An unique timestamp folder is generated each time the emma_coverager.pl is run, and the coverager.ec and coverage reports are generated and stored in this folder.
HELP

################################################################################
#                        Main                            #
################################################################################

get_input();


#get system current date
$current_date = `date '+DATE_%m_%d_%y_TIME_%H-%M-%S'`;
  chomp $current_date;


#mkdir as system current date 
$system_call = "mkdir -p $QIAN_SANDBOX/$current_date";
system $system_call;
print "created $QIAN_SANDBOX/$current_date directory\n\n";
 

#get coverage.ec
$system_call = "java -Xmx512m -cp $CODECENTER_HOME/lib/jre/lib/ext/emma.jar emma ctl -connect localhost:47653 -command coverage.get,$QIAN_SANDBOX/$current_date/coverage.ec";
system $system_call;
print "Generated currect coverage.ec\n\n";


#Run coverage report
chdir "$QIAN_SANDBOX/$current_date";
$system_call = "java -Xmx512m -cp $CODECENTER_HOME/lib/jre/lib/ext/emma.jar emma report -r txt,html -in $QIAN_SANDBOX/merged_coverage.em -in $QIAN_SANDBOX/$current_date/coverage.ec -p $CODECENTER_HOME/lib/jre/lib/ext/emma.props";
system $system_call;
print "Generated reports\n\n";


#Move files around
$system_call = "mv coverage/* $QIAN_SANDBOX/$current_date";
system $system_call;
print "Moved generated reports to $current_date directory\n\n";


#Copy generated reports to qa://var/www
$system_call = "scp -r $QIAN_SANDBOX/$current_date root\@qa://var/www/CodeCenter_coverage/";
system $system_call;
print "Copied generated reports to root\@qa\:\/\/var\/www\/CodeCenter_coverage/$current_date\n\n";


#Send e-mail with generated report
$system_call = "mail $MAILTO -s \"$current_date Code Coverage Report on 10.12.13.165 for CodeCenter\" <$QIAN_SANDBOX/$current_date/coverage.txt";
system $system_call;
print "Sent generated report to $MAILTO\n\n";


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
 