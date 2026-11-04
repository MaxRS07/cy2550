# Levels

## 9

In level 9, locked and flag look like this:
```
-rw-r-----+ 1 root            root             53 Oct 20 17:20 flag.txt
-rw-------  1 root            root             51 Oct 20 17:20 locked.txt
```
Even though I don't belong to the root group, I am still able to run `cat` on flag.txt and read the contents. After researching, I found that the `+` at the end of the permission bits of flag.txt means that there are additional permissions that are granted by an access control list (ACL). Running `getfacl` on the file reveals this file containing addtional permissions:

```
# file: flag.txt
# owner: root
# group: root
user::rw-
user:siebengartner.m:r--
group::---
mask::r--
other::---
```