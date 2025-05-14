
### InconsistentMigrationHistory

https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory



### Install SQL db

https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/


### Error of mysqlclient

(venv) PS E:\arpita\Django\Project - Blog\blogger> pip install mysqlclient
Collecting mysqlclient
  Using cached mysqlclient-2.2.7.tar.gz (91 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for mysqlclient (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [41 lines of output]
      # Options for building extension module:
        library_dirs: ['C:/mariadb-connector\\lib\\mariadb', 'C:/mariadb-connector\\lib']
        libraries: ['kernel32', 'advapi32', 'wsock32', 'shlwapi', 'Ws2_32', 'crypt32', 'secur32', 'bcrypt', 'mariadbclient']
        extra_link_args: ['/MANIFEST']
        include_dirs: ['C:/mariadb-connector\\include\\mariadb', 'C:/mariadb-connector\\include\\mysql', 'C:/mariadb-connector\\include']
        extra_objects: []
        define_macros: [('version_info', (2, 2, 7, 'final', 0)), ('__version__', '2.2.7')]
      running bdist_wheel
      running build
      running build_py
      creating build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\connections.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\converters.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\cursors.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\release.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\times.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\_exceptions.py -> build\lib.win32-cpython-38\MySQLdb
      copying src\MySQLdb\__init__.py -> build\lib.win32-cpython-38\MySQLdb
      creating build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\CLIENT.py -> build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\CR.py -> build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\ER.py -> build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\FIELD_TYPE.py -> build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\FLAG.py -> build\lib.win32-cpython-38\MySQLdb\constants
      copying src\MySQLdb\constants\__init__.py -> build\lib.win32-cpython-38\MySQLdb\constants
      running egg_info
      writing src\mysqlclient.egg-info\PKG-INFO
      writing dependency_links to src\mysqlclient.egg-info\dependency_links.txt
      writing top-level names to src\mysqlclient.egg-info\top_level.txt
      reading manifest file 'src\mysqlclient.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      adding license file 'LICENSE'
      writing manifest file 'src\mysqlclient.egg-info\SOURCES.txt'
      copying src\MySQLdb\_mysql.c -> build\lib.win32-cpython-38\MySQLdb
      running build_ext
      building 'MySQLdb._mysql' extension
      creating build\temp.win32-cpython-38\Release\src\MySQLdb
      "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\bin\HostX86\x86\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD "-Dversion_info=(2, 2, 7, 'final', 0)" -D__version__=2.2.7 -IC:/mariadb-connector\include\mariadb -IC:/mariadb-connector\include\mysql -IC:/mariadb-connector\include -IE:\arpita\Django\Project-1\venv\include -IC:\Users\Admin\AppData\Local\Programs\Python\Python38-32\include -IC:\Users\Admin\AppData\Local\Programs\Python\Python38-32\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /Tcsrc/MySQLdb/_mysql.c /Fobuild\temp.win32-cpython-38\Release\src/MySQLdb/_mysql.obj
      _mysql.c
      src/MySQLdb/_mysql.c(29): fatal error C1083: Cannot open include file: 'mysql.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.44.35207\\bin\\HostX86\\x86\\cl.exe' failed with exit code 2
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for mysqlclient
Failed to build mysqlclient
ERROR: Failed to build installable wheels for some pyproject.toml based projects (mysqlclient)
(venv) PS E:\arpita\Django\Project - Blog\blogger> 

