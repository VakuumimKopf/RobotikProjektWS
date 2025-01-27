# **Robotik - Oliver Lorenz**

## **Belegaufgabe 1 (Publisher Subscriber)**
### **Funktionsweise**
Hierbei sollten zwei Packages erstellt werden. Dabei sollte eines Publisher (in C++) und eines Subscriber (in Python) sein.
Der Publisher ist dabei im Package cpp_pubsub zu finden und der Subscriber im Package timing_tubaf_py.
Beim ausführen beider Packages hat zur Folge, dass der Publisher auf einen bestimmten Topic "number" die ganze Zeit "Hello World!" überträgt, während der Subscriber auf diesem Topic diese Nachrichten empfängt und mit entsprechender Nummer wieder ausgibt. Zusätzlich published er auf dem Topic "diff" die Zeitdifferenz der letzten beiden Nachrichten auf "number" 

### **Startanleitung**
zum ausführen öffnet man ein Terminal und navigiert in das Verzeichnis, welches die ros Packages enthält.
Anschließend führt man folgende Befehle aus:
- colcon build
- source install/local_setup.bash
- ros2 run cpp_pubsub talker
- ros2 run timing_tubaf_py listener

## **Belegaufgabe 2 (Laserfollow)**
### **Funktionsweise**

### **Startanleitung**
