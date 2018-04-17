/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 * Runs multiple servos
 */

#include <Servo.h>
#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <std_msgs/Float64>

ros::NodeHandle nh;

Servo servo1, servo2, servo3; //create servo objects to control a servo

void messageCb( const sensor_msgs::JointState& cmd_msg){

  cmd_msg_servo1 = cmd_msg.position[1];
  cmd_msg_servo2 = cmd_msg.position[2];
  cmd_msg_servo3 = cmd_msg.position[3];

  servo1.write(cmd_msg_servo1);
  servo2.write(cmd_msg_servo2);
  servo3.write(cmd_msg_servo3);

  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
}

ros::Subscriber<sensor_msgs::JointState> sub("/joint_states", &messageCb );

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

  delay(10);

}

void loop()
{
  //msg.data = cmd_msg_servo1;
  //pub.publish( msg );

  nh.spinOnce();
  delay(1);
}
