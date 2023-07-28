package com.blue.chatingapp2.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.blue.chatingapp2.R;
import com.blue.chatingapp2.model.Chat;

import java.util.ArrayList;

public class ChatAdapter extends RecyclerView.Adapter<ChatAdapter.ViewHolder>  {

    Context context;
    ArrayList<Chat> chatArrayList;

    public ChatAdapter(Context context, ArrayList<Chat> chatArrayList) {
        this.context = context;
        this.chatArrayList = chatArrayList;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.main_row, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Chat chat = chatArrayList.get(position);

        holder.txtNickname.setText(chat.nickname);
        holder.txtContent.setText(chat.contents);
        holder.txtTime.setText(chat.time);
    }

    @Override
    public int getItemCount() {
        return chatArrayList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

        TextView txtContent;
        TextView txtNickname;
        TextView txtTime;
        CardView cardView;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);

            txtContent = itemView.findViewById(R.id.txtContent);
            txtNickname = itemView.findViewById(R.id.txtNickname);
            txtTime = itemView.findViewById(R.id.txtTime);
            cardView = itemView.findViewById(R.id.cardView);

        }
    }
}
