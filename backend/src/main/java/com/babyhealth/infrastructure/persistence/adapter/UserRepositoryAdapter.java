package com.babyhealth.infrastructure.persistence.adapter;

import com.babyhealth.application.port.out.UserRepository;
import com.babyhealth.domain.identity.Role;
import com.babyhealth.domain.identity.User;
import com.babyhealth.infrastructure.persistence.entity.UserEntity;
import com.babyhealth.infrastructure.persistence.repository.UserJpaRepository;
import org.springframework.stereotype.Component;
import java.util.Optional;
import java.util.UUID;

@Component
public class UserRepositoryAdapter implements UserRepository {
    private final UserJpaRepository jpa;
    public UserRepositoryAdapter(UserJpaRepository jpa) { this.jpa = jpa; }

    @Override
    public User save(User user) {
        UserEntity e = new UserEntity(user.getId(), user.getEmail(), user.getPasswordHash(), user.getRole());
        e.setActive(user.isActive());
        jpa.save(e);
        return user;
    }

    @Override
    public Optional<User> findByEmail(String email) {
        return jpa.findByEmail(email).map(this::toDomain);
    }

    @Override
    public Optional<User> findById(UUID id) {
        return jpa.findById(id).map(this::toDomain);
    }

    private User toDomain(UserEntity e) {
        return new User(e.getId(), e.getEmail(), e.getPasswordHash(), e.getRole());
    }
}
