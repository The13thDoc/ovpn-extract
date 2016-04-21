# This Python file uses the following encoding: utf-8

'''
Extract OpenVPN certs and keys from an .ovpn configuration file.
'''

import sys
import os

# Program variables
# Full path to .ovpn file
ovpnFileName = ''
directory = os.path.dirname(ovpnFileName)

# Access the ovpn file.
def accessFile():
    ovpnFile =  open(ovpnFileName, 'r')
    print 'Directory of .ovpn: ', directory, '\n'
    content = ovpnFile.read();

    getCountryCode()
    getCA(content)
    getCert(content)
    getKey(content)

    # close it
    ovpnFile.close();


# Get country code.
def getCountryCode():
    i = ovpnFileName.index('.openvpn.frootvpn.ovpn')
    return ovpnFileName.strip()[i-2:i]

# Get CA certificate info.
def getCA(content):
    caName = getCountryCode() + '-ca.crt'
    caContent = content[content.index('<ca>'): content.index('</ca>') + 5]
    writeFile(caName, caContent)
    return 'CA', caName

# Get user cert info.
def getCert(content):
    certName = getCountryCode() + '-remote-user.crt'
    certContent = content[content.index('<cert>'): content.index('</cert>') + 7]
    writeFile(certName, certContent)
    return  'Cert', certName

# Get key.
def getKey(content):
    keyName = getCountryCode() + '.key'
    keyContent = content[content.index('<key>'): content.index('</key>') + 6]
    writeFile(keyName, keyContent)
    return  'Key', keyName

# Write the content to the file.
def writeFile(name, content):
    newFile = open(name, 'w')
    newFile.write(content)
    print os.path.abspath(newFile.name)
    newFile.close()


# Main.
def main():
    print '\nBegin extracting...\n'
    os.chdir(directory)
    accessFile()
    print '\nDone.\n'

# Run.
main()
