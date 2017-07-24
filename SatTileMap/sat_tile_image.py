import requests
from PIL import Image
from StringIO import StringIO

#SET tile_zoom_matrx TO 8
#to crash system or achieve greatness with crazy zoom in abilities 

tile_args = {1:(3,2), 2:(5,3), 3:(10,5), 4:(20,10), 5:(40,20), 6:(80,40), 7:(160,80), 8:(320,160)}

def get_tile_map(tile_zoom_matrix = 1, tile_resolution = 512, year = '2017', month = '01', day = '01'):

    tile_col_max = tile_args[tile_zoom_matrix][0]
    tile_row_max = tile_args[tile_zoom_matrix][1]
    
    result_width = tile_col_max*tile_resolution
    result_height = tile_row_max*tile_resolution

    result = Image.new('RGB', (result_width, result_height))
    i=0
    tiles_downloaded=1

    tile_sum = tile_col_max * tile_row_max

    #iterate through map rows
    while i<tile_row_max:

        j=0

        #iterate through map columns
        while j<tile_col_max:

            try:

                #get link for current tile
                link = """http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=MODIS_Terra_CorrectedReflectance_TrueColor&STYLE=&TILEMATRIXSET=250m&TILEMATRIX={}&TILEROW={}&TILECOL={}&FORMAT=image%2Fjpeg&TIME={}-{}-{}""".format(tile_zoom_matrix, i, j, year, month, day)

                #download tile
                retrieved_img = Image.open(StringIO(requests.get(link).content))
                #paste it to the big map
                result.paste(im=retrieved_img, box=(tile_resolution*j, tile_resolution*i))

                print("Downloading Tile: %s/%s"%(tiles_downloaded,tile_sum))

                j+=1
                tiles_downloaded+=1

            except Exception as e:
                pass

        i+=1
    #Return PIL Image
    return result


#TEST 
map_img = get_tile_map()
map_img.save('map.png')
