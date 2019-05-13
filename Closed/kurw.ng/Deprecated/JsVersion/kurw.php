<html>
<script>
var code = "Niech ten test to kurwa" //<?php echo $_POST['code']; ?> ;
var line = code;
var sercz;
if(/[Nn][Ii][Ee][Cc][Hh] ([^\n \t]+) [Tt][Oo] ([^\n]+)/.test(line))
{
	sercz = / ([^\n]+) /.exec(line);
	alert(sercz[0]);
	alert(sercz[2]);
}
</script>
</html>
