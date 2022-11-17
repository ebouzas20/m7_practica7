import xml.etree.ElementTree as ET

students = ET.Element('Estudiants')
student = ET.SubElement(students, 'Estudiant',)
name = ET.SubElement(students, 'Carlos')
surname = ET.SubElement(students, 'García')
email = ET.SubElement(students, 'carlosgarciacortes@gmail.com')
dni = ET.SubElement(students, '21554478A')


archivo = open('estudiants.xml', 'a')

archivo.write(ET.tostring(students, encoding='utf-8').decode('utf-8'))