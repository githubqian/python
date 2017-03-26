#! usr/bin/perl
print "What number you want to calculate the factorial?";
print "\n";

chomp ($n = <>);

my $ret = 1;
my $i;

if (($n == 0) || ($n == 1)){
print "The factorial of munber $n is $n.";
print "\n";

}

else {
for ($i = 2; $i <= $n; $i++) {
$ret = $ret * $i;
}
print "The factorial of munber $n is $ret.";
print "\n";

}
