require 'net/http'
require 'json'

def obtener_humedad
  uri = URI('http://<YOUR_CANISTER_URL>/humidity')
  response = Net::HTTP.get(uri)
  return JSON.parse(response)["humidity"]
rescue StandardError => e
  puts "Error al obtener la humedad: #{e.message}"
  return nil
end

begin
  loop do
    humidity = obtener_humedad

    # Parámetros de humedad
    if humidity
      if humidity < 50
        RPi::GPIO.set_high PIN_VALVULA
        puts "Activar válvula, no se detecta humedad suficiente (Humedad: #{humidity}%)"
      else
        RPi::GPIO.set_low PIN_VALVULA
        puts "Desactivar válvula, humedad necesaria (Humedad: #{humidity}%)"
      end
    else
      puts "Error al detectar humedad"
    end
    sleep INTERVALO_LECTURA
  end
ensure
  RPi::GPIO.clean_up
end
