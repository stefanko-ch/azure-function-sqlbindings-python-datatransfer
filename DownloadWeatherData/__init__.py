import ftplib
import io
import logging
import os
import pandas

import azure.functions as func

def main(every5Minute: func.TimerRequest, cities: func.SqlRowList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    filename = "cities.txt"
    filesize = 0

    # convert the SQL data to comma separated text
    city_list = pandas.DataFrame(cities)
    # product_csv = product_list.to_csv(index=False)
    # datatosend = io.BytesIO(product_csv.encode('utf-8'))


    print(city_list)

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

    logging.info(f"File {filename} uploaded to FTP server. Size: {filesize} bytes")
