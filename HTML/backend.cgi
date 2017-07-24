#!/usr/bin/python
print('Content-type: text/html\r\n\r')

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
input_data = cgi.FieldStorage()

print 'Content-Type:text/html' #HTML is following
print                          #Leave a blank line

# Get data from fields
name = input_data.getvalue('drugName')
excelfile = form['datafile']

# Testing if File was successully upload
if excelfile.datefile:
   fn = os.path.basename(excelfile.datafile)
   open('/tmp/' + fn, 'wb').write(excelfile.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'

print(name)
