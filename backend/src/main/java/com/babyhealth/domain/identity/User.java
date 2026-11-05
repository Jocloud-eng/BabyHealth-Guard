package com.babyhealth.domain.identity;

import com.babyhealth.domain.shared.AggregateRoot;
import java.util.UUID;

public class User extends AggregateRoot {
    private final UUID id;
    private String email;
    private String passwordHash;
    private Role role;
    private boolean active;

    public User(UUID id, String email, String passwordHash, Role role) {
        this.id = id;
        this.email = email;
        this.passwordHash = passwordHash;
        this.role = role;
        this.active = true;
    }

    public UUID getId() { return id; }
    public String getEmail() { return email; }
    public String getPasswordHash() { return passwordHash; }
    public Role getRole() { return role; }
    public boolean isActive() { return active; }
}
