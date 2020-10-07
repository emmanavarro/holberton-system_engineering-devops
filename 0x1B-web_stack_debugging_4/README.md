# 0x1B. Web stack debugging #4 

## Requirements
* Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* Puppet manifests files must end with the extension .pp
* Puppet v3.4

---

## Tasks

### [0. Sky is the limit, let's bring that limit higher](./0-the_sky_is_the_limit_not.pp)
* In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests. 

```
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
...
Concurrency Level:      100
Time taken for tests:   0.255 seconds
Complete requests:      2000
Failed requests:        1016
   (Connect: 0, Receive: 0, Length: 1016, Exceptions: 0)

root@0a62aa706eb3:/# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for 0a62aa706eb3.local in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[fix--for-nginx]/returns: executed successfully
Notice: Finished catalog run in 1.12 seconds
root@0a62aa706eb3:/#
root@0a62aa706eb3:/#
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
...
Concurrency Level:      100
Time taken for tests:   0.179 seconds
Complete requests:      2000
Failed requests:        0
```


### [1. User limit](./1-user_limit.pp)
* Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

---

## Author
* **Emma Navarro** | [Github](https://github.com/emmanavarro)
