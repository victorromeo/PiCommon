# PiCommon

A set of common utilities which are commonly used in a number of applications

Python and Shell implementations are attempting to be similar in their design to aid their use.  They are not however simple wrappers of each other, as there may be implementations which are not appropriate to be duplicated or wrapper.

| Feature     | Function                                                  | python3                                                                                  | shell          |
| ----------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------- |
| Compression | GZip                                                      | [x] compress_gzip <br> [x] decompress_gzip                                               | []             |
| Compression | BZ2                                                       | [x] compress_bz2 <br> [x] decompress_bz2                                                 | []             |
| Compression | Zip                                                       | [x] compress_zip <br> [x] decompress_zip                                                 | []             |
| Compression | TAR                                                       | [x] tar [x] tar_gz <br> [x] tar_bz2  <br> [x] untar <br> [x] untar_gz <br> [x] untar_bz2 | []             |
| Config      | Read File                                                 | [x] ReadFromFile                                                                         | []             |
| Config      | Read from JSON string                                     | [x] Read                                                                                 | []             |
| Config      | Write File                                                | [x] WriteToFile                                                                          | []             |
| Config      | Write to JSON string                                      | [x] Write                                                                                | []             |
| Config      | Get prettified JSON string                                | [x] Get                                                                                  | []             |
| Config      | Add Key Value pair                                        | [x] Add                                                                                  | []             |
| Config      | Remove Key Value pair                                     | [x] Remove                                                                               | []             |
| Cron        | Add Cron Task                                             | [X] **uses crontab*                                                                      | []             |
| Cron        | Remove Cron Task                                          | [X] **uses crontab*                                                                      | []             |
| Cron        | Enable Cron Task                                          | [X] **uses crontab*                                                                      | []             |
| Cron        | Disable Cron Task                                         | [X] **uses crontab*                                                                      | []             |
| Disk        | Make Directory                                            | [x] make_dir                                                                             | []             |
| Disk        | Remove Directory                                          | [x] remove_dir                                                                           | []             |
| Disk        | Read File                                                 | [x] remove_dir                                                                           | []             |
| Disk        | Write File                                                | [x] remove_dir                                                                           | []             |
| Disk        | File Exists                                               | [x] file_exists                                                                          | []             |
| Disk        | Directory Exists                                          | [x] directory_exists                                                                     | []             |
| Disk        | Path Exists                                               | [x] exists                                                                               | []             |
| Disk        | Owner ID                                                  | [x] owner_id                                                                             | []             |
| Disk        | Group ID                                                  | [x] group_id                                                                             | []             |
| Disk        | Disk capacity                                             | [x] size                                                                                 | []             |
| Disk        | Access Time                                               | [x] access_time                                                                          | []             |
| Disk        | Creation Time                                             | [x] creation_time                                                                        | []             |
| Disk        | Modification Time                                         | [x] modification_time                                                                    | []             |
| Disk        | Protection                                                | [x] protection                                                                           | []             |
| Disk        | inode                                                     | [x] inode                                                                                | []             |
| Disk        | Hard Link from symbolic link                              | [x] hard_links                                                                           | []             |
| Disk        | Create symbolic link                                      | [x] create_symbolic_link                                                                 | []             |
| Encryption  | Generate new RSA Public/Private keypair                   | [x] newkeys                                                                              | []             |
| Encryption  | Import RSA Public/Private keypair                         | [x] import_key                                                                           | []             |
| Encryption  | Get RSA Public Key                                        | [x] getpublickey                                                                         | []             |
| Encryption  | Encrypt message using RSA                                 | [x] encrypt                                                                              | []             |
| Encryption  | Decrypt message using RSA                                 | [x] decrypt                                                                              | []             |
| Encryption  | Sign message with RSA (SHA-512, SHA-384, SHA256, SHA-1)   | [x] sign                                                                                 | []             |
| Encryption  | Verify message with RSA (SHA-512, SHA-384, SHA256, SHA-1) | [x] verify                                                                               | []             |
| Hash        | Get sha224 hash                                           | [x] hash_sha224                                                                          | []             |
| Hash        | Get sha256 hash                                           | [x] hash_sha256                                                                          | []             |
| Hash        | Get sha384 hash                                           | [x] hash_sha384                                                                          | []             |
| Hash        | Get sha512 hash                                           | [x] hash_sha512                                                                          | []             |
| Hash        | Get md5 hash                                              | [x] hash_md5                                                                             | []             |
| OS          | List Processes                                            | []                                                                                       | [x] ps         |
| OS          | Kill Process                                              | [x] kill(pid)                                                                            | [x] kill *pid* |
| OS          | Sleep Process                                             | [x] sleep(pid)                                                                           | []             |
| OS          | Wake Process                                              | [x] wake(pid)                                                                            | []             |
| OS          | Get Current Process ID                                    | [x] pid()                                                                                | []             |
| OS          | Get Current Session ID                                    | [x] sid()                                                                                | []             |
| OS          | Get Current Parent PID                                    | [x] parent_pid()                                                                         | []             |
| OS          | Create child process                                      | [x] fork()                                                                               | []             |
