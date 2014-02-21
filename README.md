# Django-reloj-poblacional
------------------

App que implementa el algoritmo de reloj poblacional


# Dependencias

Python 

  * django

Javascript

  * jquery


# Instalar

En tu settings.py

```python
    INSTALLED_APPS = ( 
        ....    
        'inei.reloj',
    )
```


En tu urls.py

```python
    urlpatterns = patterns('',
        ....
        (r'^reloj/', include('inei.reloj.urls')),
    )
```