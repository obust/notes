# SSH

SSH, or Secure Shell, is a protocol used to securely log onto remote systems.

https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu
https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
https://www.digitalocean.com/community/tutorials/how-to-configure-custom-connection-options-for-your-ssh-client

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:1 -->

1. [SSH Password-based Authentication](#ssh-password-based-authentication)
2. [SSH Key-based Authentication](#ssh-key-based-authentication)
	1. [Generate the Public/Private Key Pair](#generate-the-publicprivate-key-pair)
	2. [Transfer the Public Key](#transfer-the-public-key)
3. [SSH Config File](#ssh-config-file)
	1. [Configuratin File Structure](#configuratin-file-structure)
	2. [Basic Connection](#basic-connection)

<!-- /TOC -->

## SSH Password-based Authentication

**Log in**:

```
ssh <username>@<remote-host>
Password:
```

**Log out**:
```
exit
```

## SSH Key-based Authentication

While a password can eventually be cracked with a brute force attack, SSH keys are nearly impossible to decipher by brute force alone. You can increase security even more by protecting the private key with a passphrase.

Key-based authentication works by creating a pair of keys:

- The **private key** is located on the client machine and is secured and kept secret.
- The **public key** is given to any remote server you wish to access.

When you attempt to connect using a key-pair, the server will use the public key to create a message for the client computer that can only be read with the private key.
The client computer then sends the appropriate response back to the server and the server will know that the client is legitimate.


### Generate the Public/Private Key Pair

```
ssh-keygen -t rsa
```

The public key is now located in `/home/demo/.ssh/id_rsa.pub`.
The private key is now located in `/home/demo/.ssh/id_rsa`.

**Using a passphrase**
It's up to you whether you want to use a passphrase.

`Enter passphrase (empty for no passphrase):`

Should a passphrase-protected private key fall into an unauthorized users possession, they will be unable to log in to its associated accounts until they figure out the passphrase, buying the hacked user some extra time. The only downside, of course, to having a passphrase, is then having to type it in each time you use the Key Pair.

### Transfer the Public Key

```sh
ssh-copy-id <username>@<remote-host>
```

Your local public key (`~/.ssh/id_rsa.pub` file) is copied to the remote server's authorized keys (`~/.ssh/authorized_keys` directory).

Now you can go ahead and login `ssh <username>@<remote-host>` and you will not be prompted for a password. However, if you set a passphrase, you will be asked to enter the passphrase at that time (and whenever else you log in in the future).

## SSH Config File

Use the SSH config file at `~/.ssh/config` to **provide customized client-side connection options**.
These can be saved to a configuration file that can be used to define per-host values. This can help keep the different connection options you use for each host separated and organized.

### Configuratin File Structure

```
Host <firsthost>
    OPTION_1 custom_value
    OPTION_2 custom_value

Host <secondhost>
    ANOTHER_OPTION custom_value

    Host *host
        ANOTHER_OPTION custom_value

    Host *
        CHANGE_DEFAULT custom_value
```

### Basic Connection

```
Host <alias>
    User <username>
    Host <remote-host>
```
