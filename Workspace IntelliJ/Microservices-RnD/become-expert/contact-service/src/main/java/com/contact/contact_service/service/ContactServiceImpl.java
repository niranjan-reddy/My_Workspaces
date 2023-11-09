package com.contact.contact_service.service;

import com.contact.contact_service.entity.Contact;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ContactServiceImpl implements ContactService{

    List<Contact> list = List.of(
            new Contact(1L, "niranjan@kayacorp.cyou", "Niranjan", 1234L),
            new Contact(2L, "delisha@kayacorp.cyou", "Delisha", 1234L),
            new Contact(3L, "teyjansh@kayacorp.cyou", "Teyjansh", 1234L),
            new Contact(4L, "teyjanshi@kayacorp.cyou", "Teyjanshi", 1234L),
            new Contact(5L, "niranjan@kayacorp.cyou", "Niranjan", 1235L),
            new Contact(6L, "delisha@kayacorp.cyou", "Delisha", 1235L),
            new Contact(7L, "teyjansh@kayacorp.cyou", "Teyjansh", 1235L),
            new Contact(8L, "teyjanshi@kayacorp.cyou", "Teyjanshi", 1235L),
            new Contact(9L, "niranjan@kayacorp.cyou", "Niranjan", 1236L),
            new Contact(10L, "delisha@kayacorp.cyou", "Delisha", 1236L),
            new Contact(11L, "teyjansh@kayacorp.cyou", "Teyjansh", 1236L),
            new Contact(12L, "teyjanshi@kayacorp.cyou", "Teyjanshi", 1236L),
            new Contact(13L, "niranjan@kayacorp.cyou", "Niranjan", 1237L),
            new Contact(14L, "delisha@kayacorp.cyou", "Delisha", 1237L),
            new Contact(15L, "teyjansh@kayacorp.cyou", "Teyjansh", 1237L),
            new Contact(16L, "teyjanshi@kayacorp.cyou", "Teyjanshi", 1237L)
    );
    @Override
    public List<Contact> getContactsOfUser(Long userId) {
        return list.stream().filter(contact -> contact.getUserId().equals(userId)).collect(Collectors.toList());
    }
}
