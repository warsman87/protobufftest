package com.example;

import java.io.*;
import java.net.Socket;

import com.example.Message.MyMessage;

public class Application {

    public static void main(String[] args) {
        // Define the host and port
        String host = "127.0.0.1";
        int port = 12345;
        
        try (Socket socket = new Socket(host, port)) {
            // Get the output stream and input stream from the socket
            OutputStream os = socket.getOutputStream();
            InputStream is = socket.getInputStream();

            // Create a new MyMessage object with content "Hello from client"
            MyMessage message = MyMessage.newBuilder()
                    .setContent("Hello from client")
                    .build();
            
            // Write the message to the output stream
            message.writeTo(os);

            // Parse the response from the input stream
            MyMessage response = MyMessage.parseFrom(is);
            System.out.println("Server response: " + response.getContent());

            // Close the output stream and input stream
            os.close();
            is.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
