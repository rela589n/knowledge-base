
Create file for your application:
```shell
nano ~/.local/share/applications/apache-directory-studio.desktop
```

Add the following content:

```shell
[Desktop Entry]
Name=Apache Directory Studio
Comment=LDAP Browser and Editor
Exec=/opt/ApacheDirectoryStudio/ApacheDirectoryStudio
Icon=/opt/ApacheDirectoryStudio/icon.xpm
Terminal=false
Type=Application
Categories=Utility;
```

Run `alt+f2` -> `r` , and then application should be available.