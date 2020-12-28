import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

	public static void main(String[] args) {
		
		try (ServerSocket server = new ServerSocket(12345)) {
			
			while (true) {
				Socket client = server.accept();
				StringBuilder inputstring = new StringBuilder();
				
				BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
				//PrintWriter out = new PrintWriter(new OutputStreamWriter(client.getOutputStream()), true);
				inputstring.append(in.readLine());
				in.close();
				client.close();
				System.out.println(inputstring);
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
