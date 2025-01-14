This was our school assignment for Databases 3.
We used SparkSQL and other technologies.

My part was S2. (Student2)
This means I did the Customer and lock dimension and added this to the Facts table.
We also had to make Analysis queries

To fill the Database so you can start this project, see the veloscripts folder.
I had to greately reduce the file size of 07_Fill_rides (original was 1.5gb which github does not allow).

I did get some remarks by the teacher:
- In the Fact_Rides I joined the customer on subscriptionId. If I had queried (joined on rides) that while getting the data I could have joined on the customerId.
- You can see in the Fact_rides the start_lock_sk and end_lock_sk is sometimes null. This happens when a scooter is used. I could have changed the join to include the already made sk for that row somehow.


