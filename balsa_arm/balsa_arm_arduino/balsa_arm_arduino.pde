/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 * Runs multiple servos
 */

#include <Servo.h>
#include <ros.h>
#include <sensor_msgs/JointState.h>
//#include <std_msgs/Float64>
#include <math.h>

ros::NodeHandle nh;

double servorad[3];
double servodeg[3];
Servo servo1, servo2, servo3; //create servo objects to control a servo

void messageCb( const sensor_msgs::JointState& cmd_msg){

  servorad[0] = cmd_msg.position[0]; //values are in radians
  servorad[1] = cmd_msg.position[1];
  servorad[2] = cmd_msg.position[2];

  servodeg[0] = (servorad[0]*180)/M_PI; //converted radians to degrees
  servodeg[1] = (servorad[1]*180)/M_PI;
  servodeg[2] = (servorad[2]*180)/M_PI;

  servo1.write(servodeg[0]);
  servo2.write(servodeg[1]);
  servo3.write(servodeg[2]);

  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}

ros::Subscriber<sensor_msgs::JointState> sub("/move_group_fake_controller_joint_states", &messageCb );

//std_msgs::Float64 msg;
//ros::Publisher pub("joint1_chatter", &msg);
//The above two lines are there if you need to publish a message in this node

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  //nh.advertise(pub)

  servo1.attach(9); //attach it to pin 9
  servo2.attach(10); //attach it to pin 10
  servo3.attach(11); //attach it to pin 11

}

void loop()
{
  //msg.data = cmd_msg_servo1;
  //pub.publish( msg );

  nh.spinOnce();
  delay(1);
}
