from pathlib import Path
from datetime import datetime


dataHoraString = str(datetime.now())

print(dataHoraString.replace(':','-').replace('.','-'))


#f = open(Path(__file__).parent.__str__()+"\\Resultado.txt", "a")
#f.write("Now the file has more content!")
#f.close()
