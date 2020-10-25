from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Ride,Dummy
from channels.db import database_sync_to_async
import json,random,math,time

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = 'API_Channel'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
    async def disconnect(self,close_code):
        pass
    async def receive(self,text_data):
        print ('>>>>',text_data)
        data_dict=json.loads(text_data)
        await self.save_data(data_dict)
        # time.sleep(10)
        await self.send('ACK')
        pass
    @database_sync_to_async
    def save_data(self,msg):
        pack_id = -1
        if not math.isnan(msg['package_id']):
            pack_id=msg['package_id']
        fai=-1
        if not math.isnan(msg['from_area_id']):
            fai=msg['from_area_id']
        tai = -1
        if not math.isnan(msg['to_area_id']):
            tai=msg['to_area_id']
        fci=-1
        if not math.isnan(msg['from_city_id']):
            fci=msg['from_city_id']
        tci=-1
        if not math.isnan(msg['to_city_id']):
            tci=msg['to_city_id']
        tdd = 'NAN'
        if not msg['to_date']==None:
            tdd=msg['to_date']
        ob = False
        if msg['online_booking']==1:
            ob=True
        mbb=False
        if msg['mobile_site_booking']==1:
            mbb=True
        fl=-1
        if not math.isnan(msg['from_lat']):
            fl=msg['from_lat']
        fll=-1
        if not math.isnan(msg['from_long']):
            fll=msg['from_long']
        tl=-1
        if not math.isnan(msg['to_lat']):
            tl=msg['to_lat']
        tll=-1
        if not math.isnan(msg['to_long']):
            tll=msg['to_long']
        cc = False
        if msg['Car_Cancellation']==1:
            cc=True
        return Ride.objects.create(
            ride_id=msg['ride_id'],
            user_id=msg['user_id'],
            vehicle_id=msg['vehicle_id'],
            package_id=pack_id,
            travel_type_id=msg['travel_type_id'],
            from_area_id =fai,
            to_area_id=tai,
            from_city_id=fci,
            to_city_id=tci,
            from_date=msg['from_date'],
            to_date=tdd,
            online_booking=ob,
            mobile_site_booking=mbb,
            booking_created=msg['booking_created'],
            from_lat=fl,
            from_long=fll,
            to_lat=tl,
            to_long=tll,
            car_cancellation=cc
        )
        # return Dummy.objects.create(
        #     x=random.randint(1,100)
        # )
