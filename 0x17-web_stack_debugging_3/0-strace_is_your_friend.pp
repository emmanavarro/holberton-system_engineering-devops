# Fix setting file in Wordpress
exec { 'settingFix':
  command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
