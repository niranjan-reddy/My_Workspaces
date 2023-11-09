package com.user.service;

import com.user.entity.User;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService{

    List<User> list = List.of(
            new User(1234L, "Niranjan Reddy", "12345678"),
            new User(1235L, "Delisha Reddy", "12345677"),
            new User(1236L, "Teyjansh Reddy", "12345676"),
            new User(1237L, "Teyjanshi Reddy", "12345675")
    );
    @Override
    public User getUser(Long id) {
        return list.stream().filter(user->user.getUserId().equals(id)).findAny().orElse(null);
    }
}
