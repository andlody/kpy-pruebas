# =======  Kurmix  =======                           _  __   www.kurmix.org   _      
# @author    Andree Ochoa <andlody@hotmail.com>     | |/ /   _ _ __ _ __ ___ (_)_  __
# @copyright 2017-2018 Andree Ochoa                 | ' / | | | '__| '_ ` _ \| \ \/ /
# @license   The MIT license                        | . \ |_| | |  | | | | | | |>  < 
# @version   1.0.0                                  |_|\_\__,_|_|  |_| |_| |_|_/_/\_\

class Config:
	#Si la pagina esta en produccion, cambiar el valor a False.
	DEV = True

	#Base de Datos | type > 1:mysql   2:postgres   3:oracle
	TYPE 		= 1;
	HOST 		= 'localhost';
	PORT 		= '3306';
	USER 		= 'root';
	PASS 		= '';
	DATABASE  	= 'kurmix';

	#Config.PORTRUN  	= 8080; //Puerto donde correra en NodeJS