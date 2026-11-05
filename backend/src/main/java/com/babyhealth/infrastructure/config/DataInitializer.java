package com.babyhealth.infrastructure.config;

import com.babyhealth.application.port.out.UserRepository;
import com.babyhealth.domain.identity.Role;
import com.babyhealth.domain.identity.User;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.babyhealth.infrastructure.security.PasswordHasher;
import java.util.UUID;

@Configuration
public class DataInitializer {
    @Bean
    CommandLineRunner seed(UserRepository users) {
        return args -> {
            if (users.findByEmail("admin@babyhealth.local").isEmpty()) {
                users.save(new User(UUID.randomUUID(), "admin@babyhealth.local",
                    PasswordHasher.hash("admin123"), Role.ADMIN));
            }
        };
    }
}
