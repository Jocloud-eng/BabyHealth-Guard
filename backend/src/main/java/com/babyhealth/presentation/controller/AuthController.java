package com.babyhealth.presentation.controller;

import com.babyhealth.application.usecase.AuthService;
import com.babyhealth.domain.identity.Role;
import com.babyhealth.domain.identity.User;
import com.babyhealth.presentation.dto.AuthDtos;
import org.springframework.web.bind.annotation.*;
import java.util.UUID;

@RestController
@RequestMapping("/api/auth")
public class AuthController {
    private final AuthService auth;
    public AuthController(AuthService auth) { this.auth = auth; }

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
}
