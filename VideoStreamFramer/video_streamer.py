from livestreamer import Livestreamer
import os



class video_streamer():										
	def __init__(self, link, filename):						
		self.livestreamer = Livestreamer()					
		self.plugin = self.livestreamer.resolve_url(link)	
		self.streams = self.plugin.get_streams()			
		self.stream = self.streams['240p']					
		self.fd = self.stream.open()						
		self.link = link									
		self.filename = filename							
		try:
			os.remove(filename)								
			open(filename, 'ab').write('')					
		except:
			open(filename, 'ab').write('')					

	def streamBin(self):									
		while True:
			try:
				self.data = self.fd.read(1024 * 1024)		

				open(self.filename, 'ab').write(self.data)	
			except Exception as ex:							
				pass
