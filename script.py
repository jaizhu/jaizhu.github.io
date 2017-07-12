file = open("input.txt", 'r')

out_string = ''

for segment in file.read().split('.'):
    out_string += segment.split(':')[0] + '@@'

out = open('hello.html', 'w')

out.write('<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">\n<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Raleway\">\n<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">')

for segment in out_string.split('@@'):
    out.write('<div class=\"w3-quarter\">')
    out.write('<i class=\"fa ' + segment + ' w3-margin-bottom w3-jumbo\"></i>')
    out.write('</div>')
    out.write('\n\n')
