import ftplib
import io
import logging
import os
import pandas

import azure.functions as func

def main(every5Minute: func.TimerRequest, cities: func.SqlRowList, outblob: func.Out[bytes]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    filename = "cities.txt"
    filesize = 0

    # convert the SQL data to comma separated text
    city_list = pandas.DataFrame(cities)
    # product_csv = product_list.to_csv(index=False)
    # datatosend = io.BytesIO(product_csv.encode('utf-8'))

    #we save the file as a utf encoded dataframe for us to save to Azure. 

    output = city_list.to_csv('cities.csv')
    # output = data_to_loaded_into_storage.to_csv(encoding="utf-8")
    outblob.set(output)

    # print(city_list)

    # get FTP connection details from app settings
    # FTP_HOST = os.environ['FTP_HOST']
    # FTP_USER = os.environ['FTP_USER']
    # FTP_PASS = os.environ['FTP_PASS']

    # connect to the FTP server
    # try:
    #     with ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS, encoding="utf-8") as ftp:
    #         logging.info(ftp.getwelcome())
    #         # use FTP's STOR command to upload the data
    #         ftp.storbinary(f"STOR {filename}", datatosend)
    #         filesize = ftp.size(filename)
    #         ftp.quit()
    # except Exception as e:
    #     logging.error(e)

    # logging.info(f"File {filename} uploaded to FTP server. Size: {filesize} bytes")


# def main(inblob: func.InputStream, outblob: func.Out[bytes]):
#     #reading in of the json file 
#     json_data = json.loads(inblob.read())
#     #lets pretend that the data we are working with is a list filled with dicts
#     data_to_loaded_into_storage = pd.Dataframe(json_data)
#     logging.info("saving data back to Azure.")
#     #we save the file as a utf encoded dataframe for us to save to Azure. 
#     output = data_to_loaded_into_storage.to_csv(encoding="utf-8")
#     outblob.set(output)