package com.babyhealth.presentation.controller;

import com.babyhealth.application.port.out.UserRepository;
import com.babyhealth.application.usecase.AuthService;
import com.babyhealth.domain.identity.User;
import jakarta.servlet.http.HttpServletRequest;
import java.util.Map;
import java.util.UUID;
import com.babyhealth.domain.identity.Role;
import com.babyhealth.domain.identity.User;
import com.babyhealth.presentation.dto.AuthDtos;
import org.springframework.web.bind.annotation.*;
import java.util.UUID;

@RestController
@RequestMapping("/api/auth")
public class AuthController {
    private final AuthService auth;
    private final UserRepository users;
    public AuthController(AuthService auth, UserRepository users) { this.auth = auth; this.users = users; }

    @PostMapping("/register")
    public AuthDtos.AuthResponse register(@RequestBody AuthDtos.RegisterRequest req) {
        Role role = Role.valueOf(req.role() == null ? "MOTHER" : req.role().toUpperCase());
        User u = auth.register(req.email(), req.password(), role);
        return new AuthDtos.AuthResponse(null);
    }

    @PostMapping("/login")
    public AuthDtos.AuthResponse login(@RequestBody AuthDtos.LoginRequest req) {
        String token = auth.login(req.email(), req.password());
        return new AuthDtos.AuthResponse(token);
    }

    @GetMapping("/me")
    public Map<String,Object> me(HttpServletRequest req) {
        String uid = (String) req.getAttribute("userId");
        if (uid == null) throw new IllegalArgumentException("Unauthorized");
        User u = users.findById(UUID.fromString(uid)).orElseThrow(() -> new IllegalArgumentException("User not found"));
        return Map.of("id", u.getId().toString(), "email", u.getEmail(), "role", u.getRole().name());
    }
}
