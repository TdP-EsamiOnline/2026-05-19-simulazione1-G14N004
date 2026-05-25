from database.DB_connect import DBConnect
from model.artista import Artista
from model.artistaPopolarita import ArtistaPopolarita
from model.genere import Genere


class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    from genre  """

        cursor.execute(query)

        for row in cursor:
            result.append(Genere(row["GenreId"],row["Name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllVertici(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.ArtistId , a.Name 
                    from Artist a , Album al , Genre g , Track t
                    where a.ArtistId = al.ArtistId and al.AlbumId =t.AlbumId and t.GenreId =g.GenreId and g.GenreId = %s 
                    GROUP by  a.ArtistId , a.Name 
                    having count(t.TrackId) >=1  """

        cursor.execute(query,(genere,))

        for row in cursor:
            result.append(Artista(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllArtistiPop():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  SELECT 
    a.ArtistId, 
    a.Name , 
    SUM(il.Quantity) AS popolarita
FROM 
    artist a, 
    album al, 
    track t, 
    invoiceline il
WHERE 
    a.ArtistId = al.ArtistId    
    AND al.AlbumId = t.AlbumId   
    AND t.TrackId = il.TrackId   
GROUP BY 
    a.ArtistId, 
    a.Name"""

        cursor.execute(query,)

        for row in cursor:
            result.append(ArtistaPopolarita(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArco(a1:Artista,a2:Artista):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT c.CustomerId, c.FirstName, c.LastName
FROM 
    customer c,
    invoice i1, invoiceline il1, track t1, album al1,
    invoice i2, invoiceline il2, track t2, album al2
WHERE c.CustomerId = i1.CustomerId AND c.CustomerId = i2.CustomerId
	AND i1.InvoiceId = il1.InvoiceId 
    AND il1.TrackId = t1.TrackId 
    AND t1.AlbumId = al1.AlbumId 
    AND al1.ArtistId = %s
    
    and i2.InvoiceId = il2.InvoiceId 
    AND il2.TrackId = t2.TrackId 
    AND t2.AlbumId = al2.AlbumId 
    AND al2.ArtistId = %s
    """

        cursor.execute(query,(a1.ArtistId,a2.ArtistId) )

        for row in cursor:
            result.append((row["CustomerId"],row["FirstName"],row["LastName"]))

        cursor.close()
        conn.close()
        return result


