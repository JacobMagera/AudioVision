reboot_script="@reboot /home/$USER/INSTALL/startup.sh"
(crontab -l; echo "$reboot_script") | crontab -
sh ./startup.sh