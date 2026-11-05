package com.babyhealth.presentation.dto;

public class AuthDtos {
    public record RegisterRequest(String email, String password, String role) {}
    public record LoginRequest(String email, String password) {}
    public record AuthResponse(String token) {}
}
