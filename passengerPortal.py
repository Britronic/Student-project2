import flet as ft
from flet import *
import sqlite3
import threading



#Flet Main function
def main (page:ft.Page):
    page.title= "Passenger Portal"
    page.theme_mode="light"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.padding=30
    page.window_bgcolor="blue"
    #----------------
    class Sitcolumn(ft.UserControl):
        def __init__(self,no):
            super().__init__()
            self.no=no
            self.Sit_Status=False

        def did_mount(self):
            self.ruuning=True
            self.th=threading.Thread(
            target=self.sitavailable,
            args=(),
            daemon=True
            )
            self.th.start()

        def will_unmount(self):
            self.running =False

        def updateSit(self, e):
            self.sit_number=self.no
            return self.sit_number
        def sitavailable(self):
            conn=sqlite3.connect('MoyaleBus.db')
            cursor=conn.cursor()
            self.sit_status=""
            self.sit_check=self.no
            #cursor.execute("SELECT * FROM passengers WHERE Sit_number =?",(self.sit_check,))
            cursor.execute("SELECT Sit_number FROM passengers")
            self.data=cursor.fetchall()
            for self.value in self.data:
                if self.value[0] == self.no:
                    self.Sit_Status=True
                else:
                        self.Sit_Status=False
            print(self.data)
            print(self.Sit_Status)
            self.update
        def build(self):
            self.button = ft.ElevatedButton(f"{self.no}",on_click=self.updateSit, disabled=self.Sit_Status)
            #self.button=ft.Text(f"{self.data}")
            return self.button 

    
    #______________
    #BOOK NOW BUTTON
    def bookNow(e):
        #Collect all the information from the field
        from_content=departure.value #From
        to_content=arrival.value#To
        sit_number_content=sit.value#Sit Number
        #route_cost=0#Cost
        fullname_content=fullName.value #First and Last Name
        idnumber_content=idno.value #ID Number
        phonenumber_content=phoneno.value #Phone Number
        email_content=email.value #Email
        #Dialog




        
        #VALIDATION
        if not departure.value:
            departure.error_text
            page.update()
        elif not arrival.value:
            arrival.error_text="Arrival Missing"
            page.update()
        #___________
        if from_content=="" or to_content == "" or fullname_content=="" or idnumber_content=="" or phonenumber_content=="" or email_content=="":
            print("Missing Fields")
            
        else:
            conn =sqlite3.connect('MoyaleBus.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO passengers(From_town,To_town,Sit_number,Full_name,Id_number,phone_number,email) VALUES(?,?,?,?,?,?,?)",
                           (from_content,to_content,sit_number_content,fullname_content,idnumber_content,phonenumber_content,email_content))
            conn.commit()
            conn.close()
            print(f"{from_content} {to_content} {sit_number_content} {fullname_content} {idnumber_content} {phonenumber_content} {email_content}")
            page.go("/bookingdetails")

    
        #page.go("/booksit")
        #lambda _:page.go("/booksit")
    ##Getting List of seats booked
    bookedsit=[]
    listview=ft.ListView()
    def sitavailable(e):
            conn=sqlite3.connect('MoyaleBus.db')
            cursor=conn.cursor()
            #sit_status=""
            cursor.execute("SELECT Sit_number FROM passengers")
            data=[row[0] for row in cursor.fetchall()]
            bookedsit=data
            print(bookedsit)
            page.update()
    for i in bookedsit:
        listviw.controls.append(ft.Text(f"Seat {i}"))
        page.update()
        
            
                
            
                
            
    #Remarks Section
    remarks=ft.TextField(hint_text="Your Remarks")
    contact=ft.TextField(hint_text="Your Contact")
    def sendRemarks(e):
        remarksvalue=remarks.value
        contactvalue=contact.value
        conn=sqlite3.connect('MoyaleBus.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO RemarksTable(remarks,phoneno) VALUES (?,?)",(remarksvalue,contactvalue))
        conn.commit()
        conn.close


        
    
#Define Controls
    head=ft.Text("Bus Online Booking Portal", weight="bold",size=20)
    head1=ft.Text("Choose Your Route & Site Below",weight="bold")
    departure=ft.TextField(hint_text="From",width=300,border="underline")
    arrival=ft.TextField(hint_text="To",width=300,border='underline')
    book_sit=ft.ElevatedButton("Check Available",on_click=lambda _:page.go("/booksit"))
    sit=ft.TextField(hint_text="Book A Sit",width=300,border='underline')
    head2=ft.Text("Fill Your Details To Complete The Booking",weight="bold")           
    fullName=ft.TextField(hint_text="Full Name",width=300,border='underline')
    idno=ft.TextField(hint_text="Id Number",width=300,border='underline')
    phoneno=ft.TextField(hint_text="Phone Number",width=300,border='underline')
    email=ft.TextField(hint_text="Email",width=300,border='underline')
    book=ft.ElevatedButton("Book Now",on_click=bookNow)
    
    parcelexit=ft.ElevatedButton("Exit",on_click=lambda _:page.go("/"))



    #Navigation Bar
    def changetab(e):
        #Get index tab
        my_index=e.control.selected_index
        if my_index == 0 :
            page.go("/remarks")
        elif my_index == 1:
            page.go("/bookingdetails")
        elif my_index == 2:
            page.go("/aboutUs")
        else:
            print("No tab")
    navBar= ft.NavigationBar(
        selected_index=0,
        on_change=changetab,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,label="Remarks"),
            ft.NavigationDestination(icon=ft.icons.BORDER_OUTER_ROUNDED,label="Receipt"),
            ft.NavigationDestination(icon=ft.icons.LOGOUT_ROUNDED,label="About Us")
            ]

        )
    # Front Page
    landPageBody=Container(
        Row([
            Container(
                      Image(
                          src="Bus1.png",
                          fit=ft.ImageFit.CONTAIN,
                          
                          )
                      ),
        Container(
            Column([
                Container(
                    Column([
                        Text("Moyale Liner Transport Company",color='black',weight='w900',text_align='center',size=30),
                        Row([
                            Container(width=70),
                            Text("Here at your service",color='black',weight='w600',text_align='center',size=20)
                            ]),
                        ])
                    ),
                Container(height=35),
                Container(
                    Row([
                        Container(width=70),
                        Text("Choose a Service",color='black',weight='w600',text_align='center',size=20)
                        ])
                    ),
                Container(height=2),
                Container(
                    Row([
                        Column([
                            TextButton(text="Parcel",content= Image(src="parcel.png",width=90),on_click=lambda _:page.go("/parcelPage")),
                            Text("Send Parcel",color='black',weight='w600',text_align='center')
                            ]),
                        Container(width=15),
                        Column([
                            TextButton(text="Book",content= Image(src="book.png",width=90),on_click=lambda _:page.go("/bookingPage")),
                            Text("Book Seat",color='black',weight='w600',text_align='center')
                            ]),
                        ]),
                    ),
                ]),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=5,
            border_radius=11,
            width=400,
            ),
        ]),

        
        bgcolor=ft.colors.WHITE,
        padding=5,
        width=1500,
        height=660,
        border_radius=35,
        alignment=alignment.Alignment(0.5,0.5)

        )
    ##Main Page
    mainPageBody=Container(
        Row([
            Container(
                      Image(
                          src="Bus2.png",
                          fit=ft.ImageFit.CONTAIN
                          )
                      ),
            Container(
                Column([
                    head,head1,
                    departure,arrival,
                    sit,book_sit,head2,
                    fullName,idno,
                    phoneno,email,
                    Row([book,parcelexit]),
                    navBar
                
                ]),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=1,
                border_radius=5,
                width=450,
                
                
                )

            ]),

                  
             
        bgcolor=ft.colors.WHITE,
        padding=5,
        width=1500,
        height=660,
        border_radius=35,
        alignment=alignment.Alignment(0.5,0.5)
        )
    #About us
    aboutUsBody=Container(
        Row([
            Container(
                      Image(
                          src="Bus3.png",
                          fit=ft.ImageFit.CONTAIN
                          )
                      ),
            Container(
                Column([
                Text("ABOUT US",weight="w900",size=30,color='black'),
                Text("Welcome to Moyale Liner, your one-stop \ndestination for convenient and hasle free bus booking.\nWe are dedicated to simplify your travel experience\n by provinding a seamless platform to book your ticket online",
                     color="black",size=15),
                Text("At Moyale Liner,we're commited to making your travel dreams a reality",
                     color="black",size=15),
                Container(height=1),
                Text("MOYALE LINER ROUTE",weight="w900",size=20,color='black'),
                Text("Daily Departure From Moyale : 08:00am",color="black",size=15),
                Text("Moyale To Marsabit",color="black",size=15),
                Text("Moyale To Isiolo",color="black",size=15),
                Text("Moyale To Nairobi",color="black",size=15), 
                Text("Daily Departure From Nairobi : 8:00pm",color="black",size=15),
                Text("Nairobi To Isiolo",color="black",size=15),
                Text("Nairobi To Marsabit",color="black",size=15),
                Text("Nairobi To Moyale",color="black",size=15),
                Text("OFFICE CONTACT",weight="w900",size=20,color='black'),
                Text("Nairobi Office: 0101 688 150",color="black",size=15),
                Text("Moyale Office: 0705 628 936",color="black",size=15),
                ElevatedButton("Go Back",on_click=lambda _:page.go("/bookingPage"))
                
                
                ]),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=5,
                border_radius=11,
                width=400,
                ),
            ]),

                  
             
        bgcolor=ft.colors.WHITE,
        padding=5,
        width=1500,
        height=660,
        border_radius=35,
        alignment=alignment.Alignment(0.5,0.5)
        )
    #Remark Body
    remarksBody=Container(
        Column([
            Text("Remarks Booth",weight='w900',size=25),
            Text("We would appreciate your comment or remarks on our services",weight='w600'),
            remarks,contact,
            ElevatedButton("Send Remarks",color='black',on_click=sendRemarks)
            
            ]),
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=5,
        border_radius=11,
        width=400,
        )
    #Parcel Page
    def parcelStatus(e):
        print(parcelNo.value)
    parcelhead=ft.Text("Moyale Linear Parcel Portal", weight="bold",size=20)
    parcelhead1=ft.Text("Enter Your Parcel No ",weight="bold")
    parcelNo=ft.TextField(hint_text="Parcel No",width=300,border='underline')

    class displayParcelStatus(ft.UserControl):
        def build(self):
            self.parcelType=""
            self.parcelNumber=""
            self.departure=""
            self.arrival=""
            self.status=""
            parcelType_text=ft.Text(self.parcelType,color='black',weight='bold')
            parcelNumber_text=ft.Text(self.parcelNumber,color='black',weight='bold')
            departure_text=ft.Text(self.departure,color='black',weight='bold')
            arrival_text=ft.Text(self.arrival,color='black',weight='bold')
            status_text=ft.Text(self.status,color='black',weight='bold')

            def updateDetails(e):
                query=parcelNo.value
                conn=sqlite3.connect('MoyaleBus.db')
                cursor=conn.cursor()
                cursor.execute("SELECT parcelType,parcelNo,departurePoint,arrivalPoint,status FROM parcelTable WHERE parcelNo=?",(query,))
                data=cursor.fetchone()
                parcelType_value,parcelNumber_value,departure_value,arrival_value,status_value=data
                self.parcelType=parcelType_value
                self.parcelNumber=parcelNumber_value
                self.departure=departure_value
                self.arrival=arrival_value
                self.status=status_value
                parcelType_text.value=self.parcelType
                parcelNumber_text.value=self.parcelNumber
                departure_text.value=self.departure
                arrival_text.value=self.arrival
                status_text.value=self.status 
                print(parcelType_value)
                conn.commit()
                conn.close()
                self.update()

            return Column([
                Row([
                    Text("PARCEL TYPE:",color='black',weight='bold'),
                    parcelType_text,
                    Container(height=50)
                    ]),
                Row([
                    Text("PARCEL NUMER:",color='black',weight='bold'),
                    parcelNumber_text,
                    Container(height=50)
                    ]),
                Row([
                    Text("DEPARTURE POINT:",color='black',weight='bold'),
                    departure_text,
                    Container(height=50)
                    ]),
                Row([
                    Text("ARRIVAL POINT:",color='black',weight='bold'),
                    arrival_text,
                    Container(height=50)
                    ]),
                Row([
                    Text("PARCEL STATUS:",color='black',weight='bold'),
                    status_text,
                    Container(height=50)
                    ]),
                ElevatedButton("CHECK PARCEL STATUS",on_click=updateDetails)

                ])
    
    parcelBodyPage=Container(
        Row([
            Container(
                      Image(
                          src="Bus2.png",
                          fit=ft.ImageFit.CONTAIN
                          )
                      ),
            Container(
                Column([
                    parcelhead,
                    parcelhead1,
                    parcelNo,
                    displayParcelStatus()
                   # ElevatedButton("CHECK PARCEL STATUS",on_click=parcelStatus)
                    
                    
                
                ]),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=1,
                border_radius=5,
                width=450,
                
                
                )

            ]),

                  
             
        bgcolor=ft.colors.WHITE,
        padding=5,
        width=1500,
        height=660,
        border_radius=35,
        alignment=alignment.Alignment(0.5,0.5)
        )
#______________    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    #ft.ElevatedButton("print",on_click=sitavailable),
                    landPageBody
                    #mainPageBody
                                   
                    ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"

                )

            )
        if page.route=="/bookingPage":
            page.views.append(
                ft.View(
                    "/bookingPage",
                    [
                        mainPageBody
                        ]
                    ),
                ),
            page.update()
            
        #ROUTE COST
        transportcost=0
        stopovers=""
        if departure.value == "Moyale" and arrival.value=="Marsabit":
            transportcost=1500
            stopovers=" First Stop Over  "
        elif departure.value == "Moyale" and arrival.value=="Isiolo":
            transportcost=2000
            stopovers="First Stop Over: Marsabit for 30 MIns"
        elif departure.value == "Moyale" and arrival.value=="Nairobi":
            transportcost=3000
            stopovers="First Stop Over: Marsabit for 30 Mins \nSecond Stop Over: Isiolo 1hr 30Min for Lunch"
        elif departure.value == "Nairobi" and arrival.value=="Isiolo":
            transportcost=2000
            stopovers="First Stop Over: Sagana"
        elif departure.value == "Nairobi" and arrival.value=="Marsabit":
            transportcost=2500
            stopovers="First Stop Over: Sagana for 30Min \nSecond Stop Over: Isiolo 2hrs for lunch"
        elif departure.value == "Nairobi" and arrival.value=="Moyale":
            transportcost=3000
            stopovers="First Stop Over: Sagana for 30Min \nSecond Stop Over: Isiolo 2hrs for lunch \nThird Stop Over: Marsabit for 1hr"
        else:
            print("Route Not Choosen")
            
        if page.route=="/parcelPage":
            page.views.append(
                ft.View(
                    "/parcelPage",
                    [
                        parcelBodyPage
                        ]
                    ),

                )
            page.update()
         
        
        if page.route== "/bookingdetails":
            page.views.append(
                ft.View(
                    "/bookingdetails",
                    [
                        ft.AppBar(title=ft.Text("Booking Summary"),bgcolor=ft.colors.BLUE_100),
                        ft.Text("------------------------------------------"),
                        ft.Text("YOUR TICKET DETAILS",weight="bold"),
                        ft.Text(f"Your Route: FROM: {departure.value} TO: {arrival.value}"),
                        ft.Text(f"Transport Cost:{transportcost}"),
                        ft.Text("Journey Details:"),
                        ft.Text(f"{stopovers}"),
                        ft.Text(f"Ticket: ML{idno.value}"),
                        ft.Text("Pay onboard and Carry your original ID"),
                        ft.Text("Please be on time"),
                        ft.Text("Failure to come or lateness your booking will be canceled"),
                        ft.Text("------------------------------------------"),
                        ft.ElevatedButton("Go Back", on_click =lambda _:page.go("/bookingPage")) 
                         ],             
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )
                )
            page.update()
        if page.route=="/remarks":
            page.views.append(
                ft.View(
                    "/remarks",
                    [
                        ft.Text("LEAVE YOUR REMARKS OR COMMENTS",weight="bold"),
                        remarksBody,
                        ft.ElevatedButton("Go Back", on_click =lambda _:page.go("/bookingPage")) 

                        ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"
                    )


                )
            page.update()
        if page.route=="/aboutUs":
            page.views.append(
                ft.View(
                    "/aboutUs",
                    [
                        aboutUsBody,
                        
                        ]
                    )
                )
            page.update()
        if page.route=="/booksit":
            #----

            #---
            page.views.append(
                ft.View(
                    "/booksit",
                    [
                    ft.Text("CHECK AVAILABLE SIT FROM THE SIT MAP", weight="bold",size=25),
                    #ft.TextField(hint_text="Book A Sit",width=300,border=20),
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.ElevatedButton("1"),ft.ElevatedButton("4"),ft.ElevatedButton("7"),
                                ft.ElevatedButton("10"),ft.ElevatedButton("13"),ft.ElevatedButton("16"),
                                ft.ElevatedButton("19"),ft.ElevatedButton("22"),ft.ElevatedButton("25"),
                                ft.ElevatedButton("28"),ft.ElevatedButton("31"),ft.ElevatedButton("34"),
                                ft.ElevatedButton("37"),ft.ElevatedButton("40"),ft.ElevatedButton("43"),
                                ft.ElevatedButton("46"),ft.ElevatedButton("49")

                            ]),
                            ft.Column([
                                ft.ElevatedButton("2"),ft.ElevatedButton("5"),ft.ElevatedButton("8"),
                                ft.ElevatedButton("11"),ft.ElevatedButton("14"),ft.ElevatedButton("17"),
                                ft.ElevatedButton("20"),ft.ElevatedButton("23"),ft.ElevatedButton("26"),
                                ft.ElevatedButton("29"),ft.ElevatedButton("32"),ft.ElevatedButton("35"),
                                ft.ElevatedButton("38"),ft.ElevatedButton("41"),ft.ElevatedButton("44"),
                                ft.ElevatedButton("47"),ft.ElevatedButton("50")
                            ]),
                            #ft.ElevatedButton("51"),
                            ft.Container(height=150,width=50),
                            ft.Column([
                                ft.ElevatedButton("3"),ft.ElevatedButton("6"),ft.ElevatedButton("9"),
                                ft.ElevatedButton("12"),ft.ElevatedButton("15"),ft.ElevatedButton("18"),
                                ft.ElevatedButton("21"),ft.ElevatedButton("24"),ft.ElevatedButton("27"),
                                ft.ElevatedButton("30"),ft.ElevatedButton("33"),ft.ElevatedButton("36"),
                                ft.ElevatedButton("39"),ft.ElevatedButton("42"),ft.ElevatedButton("45"),
                                ft.ElevatedButton("48"),ft.ElevatedButton("52")
                            ]),
                            ft.Row([
                                #ft.ElevatedButton("49"),ft.ElevatedButton("50"),
                                #ft.ElevatedButton("51"),ft.ElevatedButton("52")
                                ]),
                            Container(width=10),
                            ft.Column([
                            ft.Text("List of Booked Sits",weight='w900',size=20,color='black'),
                            ft.ElevatedButton("Show Booked Sit",on_click=sitavailable),
                            ft.Text(f"{bookedsit}"),
                            listview
                            
                            
                            ])
                            
                        ]),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        padding=5,
                        width=870,
                        height=900,
                        border_radius=35,
                        alignment=alignment.Alignment(0.5,0.5),
                    
                        ),
                    ft.ElevatedButton("Go Back", on_click =lambda _:page.go("/")) 
                    ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center"

                    )

                )


    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)

        
    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)
            
    #page.add(container)
    page.update()




#if __name__ == __"main"__
ft.app(target=main)
