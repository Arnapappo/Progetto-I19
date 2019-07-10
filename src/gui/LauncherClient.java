package gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class LauncherClient extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("Home.fxml"));

        primaryStage.setTitle("Ristorante");
        primaryStage.setScene(new Scene(root));
        primaryStage.show();

//        Stage secondStage = new Stage();
//        Parent cucina = FXMLLoader.load(getClass().getResource("Cucina.fxml"));
//        secondStage.setTitle("Cucina");
//        secondStage.setScene(new Scene(cucina));
//        secondStage.show();
//
//        Stage thirdStage = new Stage();
//        Parent caffetteria = FXMLLoader.load(getClass().getResource("Caffetteria.fxml"));
//        thirdStage.setTitle("Caffetteria");
//        thirdStage.setScene(new Scene(caffetteria));
//        thirdStage.show();
    }
}