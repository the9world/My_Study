package com.blue.chatingapp2.model;

public class Chat {

    public String nickname;
    public String contents;
    public String time;

    public Chat(String nickname, String contents, String time) {
        this.nickname = nickname;
        this.contents = contents;
        this.time = time;
    }

    public Chat(){

    }
}
