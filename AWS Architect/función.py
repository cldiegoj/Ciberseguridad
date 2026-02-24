def lambda_handler(event, context):
 nombre = event.get('queryStringParameters', {}).get('nombre',
'Mundo')
 mensaje = f"Hola {nombre}, desde AWS Lambda!"
 return {
 'statusCode': 200,
 'body': mensaje
 }

"""
{
  "queryStringParameters": {
    "nombre": "Carlos"
  }
}
"""