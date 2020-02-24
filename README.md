# PiCommon

A set of common utilities which are commonly used in a number of applications

## Goal

The Raspberry PI has several under-documented utilities which are not commonly known, and are therefore under-utilized.
These features will be documented by providing real implementations of their use.

Furthermore, the function set will be stabilized to provide consistent Raspberry PI configuration, and detect variation from an expected configuration.

## Implementation

Python and Shell implementations are attempting to be similar in their design to aid their use.  They are not however simple wrappers of each other, as there may be implementations which are not appropriate to be duplicated or wrapper.

Note: naming conventions will stabilize such that:

- methods and functions are lower_case with words separated by underscore character
- classes are camel upperCase
- names will express what is achieved, rather than declare the underlying implementation, as these are subject to change

| Feature     | Function                                                  | python3                                                                                  | shell          |
| ----------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------- |
| Compression | GZip                                                      | :heavy_check_mark: compress_gzip <br> :heavy_check_mark: decompress_gzip                                               | :heavy_minus_sign:             |
| Compression | BZ2                                                       | :heavy_check_mark: compress_bz2 <br> :heavy_check_mark: decompress_bz2                                                 | :heavy_minus_sign:             |
| Compression | Zip                                                       | :heavy_check_mark: compress_zip <br> :heavy_check_mark: decompress_zip                                                 | :heavy_minus_sign:             |
| Compression | TAR                                                       | :heavy_check_mark: tar :heavy_check_mark: tar_gz <br> :heavy_check_mark: tar_bz2  <br> :heavy_check_mark: untar <br> :heavy_check_mark: untar_gz <br> :heavy_check_mark: untar_bz2 | :heavy_minus_sign:             |
| Config      | Read File                                                 | :heavy_check_mark: ReadFromFile                                                                         | :heavy_minus_sign:             |
| Config      | Read from JSON string                                     | :heavy_check_mark: Read                                                                                 | :heavy_minus_sign:             |
| Config      | Write File                                                | :heavy_check_mark: WriteToFile                                                                          | :heavy_minus_sign:             |
| Config      | Write to JSON string                                      | :heavy_check_mark: Write                                                                                | :heavy_minus_sign:             |
| Config      | Get prettified JSON string                                | :heavy_check_mark: Get                                                                                  | :heavy_minus_sign:             |
| Config      | Add Key Value pair                                        | :heavy_check_mark: Add                                                                                  | :heavy_minus_sign:             |
| Config      | Remove Key Value pair                                     | :heavy_check_mark: Remove                                                                               | :heavy_minus_sign:             |
| Cron        | Add Cron Task                                             | :heavy_check_mark: **uses crontab*                                                                      | :heavy_minus_sign:             |
| Cron        | Remove Cron Task                                          | :heavy_check_mark: **uses crontab*                                                                      | :heavy_minus_sign:             |
| Cron        | Enable Cron Task                                          | :heavy_check_mark: **uses crontab*                                                                      | :heavy_minus_sign:             |
| Cron        | Disable Cron Task                                         | :heavy_check_mark: **uses crontab*                                                                      | :heavy_minus_sign:             |
| Disk        | Make Directory                                            | :heavy_check_mark: make_dir                                                                             | :heavy_minus_sign:             |
| Disk        | Remove Directory                                          | :heavy_check_mark: remove_dir                                                                           | :heavy_minus_sign:             |
| Disk        | Read File                                                 | :heavy_check_mark: remove_dir                                                                           | :heavy_minus_sign:             |
| Disk        | Write File                                                | :heavy_check_mark: remove_dir                                                                           | :heavy_minus_sign:             |
| Disk        | File Exists                                               | :heavy_check_mark: file_exists                                                                          | :heavy_minus_sign:             |
| Disk        | Directory Exists                                          | :heavy_check_mark: directory_exists                                                                     | :heavy_minus_sign:             |
| Disk        | Path Exists                                               | :heavy_check_mark: exists                                                                               | :heavy_minus_sign:             |
| Disk        | Owner ID                                                  | :heavy_check_mark: owner_id                                                                             | :heavy_minus_sign:             |
| Disk        | Group ID                                                  | :heavy_check_mark: group_id                                                                             | :heavy_minus_sign:             |
| Disk        | Disk capacity                                             | :heavy_check_mark: size                                                                                 | :heavy_minus_sign:             |
| Disk        | Access Time                                               | :heavy_check_mark: access_time                                                                          | :heavy_minus_sign:             |
| Disk        | Creation Time                                             | :heavy_check_mark: creation_time                                                                        | :heavy_minus_sign:             |
| Disk        | Modification Time                                         | :heavy_check_mark: modification_time                                                                    | :heavy_minus_sign:             |
| Disk        | Protection                                                | :heavy_check_mark: protection                                                                           | :heavy_minus_sign:             |
| Disk        | inode                                                     | :heavy_check_mark: inode                                                                                | :heavy_minus_sign:             |
| Disk        | Hard Link from symbolic link                              | :heavy_check_mark: hard_links                                                                           | :heavy_minus_sign:             |
| Disk        | Create symbolic link                                      | :heavy_check_mark: create_symbolic_link                                                                 | :heavy_minus_sign:             |
| Encryption  | Generate new RSA Public/Private keypair                   | :heavy_check_mark: newkeys                                                                              | :heavy_minus_sign:             |
| Encryption  | Import RSA Public/Private keypair                         | :heavy_check_mark: import_key                                                                           | :heavy_minus_sign:             |
| Encryption  | Get RSA Public Key                                        | :heavy_check_mark: getpublickey                                                                         | :heavy_minus_sign:             |
| Encryption  | Encrypt message using RSA                                 | :heavy_check_mark: encrypt                                                                              | :heavy_minus_sign:             |
| Encryption  | Decrypt message using RSA                                 | :heavy_check_mark: decrypt                                                                              | :heavy_minus_sign:             |
| Encryption  | Sign message with RSA (SHA-512, SHA-384, SHA256, SHA-1)   | :heavy_check_mark: sign                                                                                 | :heavy_minus_sign:             |
| Encryption  | Verify message with RSA (SHA-512, SHA-384, SHA256, SHA-1) | :heavy_check_mark: verify                                                                               | :heavy_minus_sign:             |
| Hash        | Get sha224 hash                                           | :heavy_check_mark: hash_sha224                                                                          | :heavy_minus_sign:             |
| Hash        | Get sha256 hash                                           | :heavy_check_mark: hash_sha256                                                                          | :heavy_minus_sign:             |
| Hash        | Get sha384 hash                                           | :heavy_check_mark: hash_sha384                                                                          | :heavy_minus_sign:             |
| Hash        | Get sha512 hash                                           | :heavy_check_mark: hash_sha512                                                                          | :heavy_minus_sign:             |
| Hash        | Get md5 hash                                              | :heavy_check_mark: hash_md5                                                                             | :heavy_minus_sign:             |
| OS          | List Processes                                            | :heavy_minus_sign:                                                                                       | :heavy_check_mark: ps         |
| OS          | Kill Process                                              | :heavy_check_mark: kill(pid)                                                                            | :heavy_check_mark: kill *pid* |
| OS          | Sleep Process                                             | :heavy_check_mark: sleep(pid)                                                                           | :heavy_minus_sign:             |
| OS          | Wake Process                                              | :heavy_check_mark: wake(pid)                                                                            | :heavy_minus_sign:             |
| OS          | Get Current Process ID                                    | :heavy_check_mark: pid()                                                                                | :heavy_minus_sign:             |
| OS          | Get Current Session ID                                    | :heavy_check_mark: sid()                                                                                | :heavy_minus_sign:             |
| OS          | Get Current Parent PID                                    | :heavy_check_mark: parent_pid()                                                                         | :heavy_minus_sign:             |
| OS          | Create child process                                      | :heavy_check_mark: fork()                                                                               | :heavy_minus_sign:             |
