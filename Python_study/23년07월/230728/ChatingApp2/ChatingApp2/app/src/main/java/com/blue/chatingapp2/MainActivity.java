package com.blue.chatingapp2;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.blue.chatingapp2.adapter.ChatAdapter;
import com.blue.chatingapp2.model.Chat;
import com.google.firebase.firestore.FirebaseFirestore;

import java.util.ArrayList;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity {

    EditText editContent;
    Button button;
    RecyclerView recyclerView;
    ChatAdapter adapter;
    ArrayList<Chat> chatArrayList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editContent = findViewById(R.id.editContent);
        button = findViewById(R.id.button);

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));

        FirebaseFirestore db = FirebaseFirestore.getInstance();

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String nickname = "홍길동";
                String content = editContent.getText().toString().trim();

                Calendar calendar = Calendar.getInstance();
                String time = calendar.get(Calendar.HOUR_OF_DAY) + ":" + calendar.get(Calendar.MINUTE);

                Chat chat = new Chat(nickname, content, time);
                db.collection("messages").document("chat").set(chat);
                Log.i("hi", db.collection("messges")+"");

                editContent.setText("");

                chatArrayList.add(chat);
                adapter = new ChatAdapter(MainActivity.this, chatArrayList);
                recyclerView.setAdapter(adapter);
            }
        });
    }
}