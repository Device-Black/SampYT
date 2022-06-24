<?php

$url = 'invalid url';

if(isset($_GET['uuid']))
{
    $url = 'https://www.youtube.com/watch?v='.$_GET['uuid'];
}
else if(isset($_GET['name']))
{
	$command = 'python search.py "'.$_GET['name'].'"';
    $url = shell_exec($command);
}
else
{
	echo "SampYT by DeviceBlack";
	return 1;
}

if($url != 'invalid url')
{
	$uuid = rand(1, 999999);
	
	$file = fopen("args.txt", "w");
	fwrite($file, "{$url}{$uuid}");
	fclose($file);
	
	shell_exec("python download.py");

	if(file_exists('Audio/'.$uuid.'.mp3'))
	{
		echo 'Audio/'.$uuid.'.mp3';
	}
	else echo 'download error';
}
else echo $url;

?>

