void __get_stamp(w2c_main *instance, u32 var_p0, u32 var_p1, u32 var_p2, u32 var_p3, u32 var_p4)
{
    u32 var_l5 = 0, var_l6 = 0, var_l7 = 0, var_l8 = 0, var_l9 = 0;
    u64 var_l10 = 0;
    FUNC_PROLOGUE;
    u32 var_i0, var_i1, var_i2, var_i3;
    u64 var_j0, var_j1, var_j2;
    var_i0 = instance->w2c_g0;
    var_i1 = 176u;
    var_i0 -= var_i1;
    var_l5 = var_i0;
    instance->w2c_g0 = var_i0;
    var_i0 = var_l5;
    var_i1 = 1055596u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 24, var_i1);
    var_i0 = var_l5;
    var_i1 = 1u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 28, var_i1);
    var_i0 = var_l5;
    var_i1 = 128u;
    var_i0 += var_i1;
    var_i1 = var_p4;
    w2c_main_f145(instance, var_i0, var_i1);
    var_i0 = var_l5;
    var_i1 = var_p3;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 52, var_i1);
    var_i0 = var_l5;
    var_i1 = 0u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 60, var_i1);
    var_i0 = var_l5;
    var_i1 = 1049312u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 56, var_i1);
    var_i0 = w2c_main_f494(instance);
    var_p3 = var_i0;
    var_i0 = var_l5;
    var_i1 = 0u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 40, var_i1);
    var_i0 = var_l5;
    var_j1 = 4294967296ull;
    i64_store(&instance->w2c_memory, (u64)(var_i0) + 32, var_j1);
    var_i0 = 8u;
    var_l6 = var_i0;
    while (var_i0)
    {
        var_i0 = var_l5;
        var_i1 = 32u;
        var_i0 += var_i1;
        var_i1 = 0u;
        var_i2 = 8u;
        w2c_main_f335(instance, var_i0, var_i1, var_i2);
        var_i0 = var_p3;
        var_i1 = 264u;
        var_i0 += var_i1;
        var_l7 = var_i0;
        var_i0 = var_p3;
        var_i1 = 328u;
        var_i0 += var_i1;
        var_l9 = var_i0;
        while (var_p4 >= 64u)
        {
            var_j0 = i64_load(&instance->w2c_memory, (u64)(var_p3) + 320u);
            var_l10 = var_j0;
            var_j1 = 1ull;
            if ((s64)var_j0 >= (s64)var_j1)
            {
                var_i0 = var_l9;
                var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0));
                var_i1 = 0u;
                if ((s32)var_i0 >= (s32)var_i1)
                {
                    var_i0 = var_p3;
                    var_j1 = var_l10;
                    var_j2 = 18446744073709551360ull;
                    var_j1 += var_j2;
                    i64_store(&instance->w2c_memory, (u64)(var_i0) + 320, var_j1);
                    var_i0 = var_l7;
                    var_i1 = var_p3;
                    w2c_main_f106(instance, var_i0, var_i1);
                }
            }
            var_i0 = var_p3;
            var_i1 = 0u;
            i32_store(&instance->w2c_memory, (u64)(var_i0) + 256, var_i1);
            var_p4 = 0u;
        }
        while (var_p4 < 64u)
        {
            var_i0 = var_p3;
            var_i1 = var_p4;
            var_i2 = 2u;
            var_i1 <<= (var_i2 & 31);
            var_i0 += var_i1;
            var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0));
            var_l8 = var_i0;
            var_i0 = var_p3;
            var_i1 = var_p4;
            var_i2 = 1u;
            var_i1 += var_i2;
            var_p4 = var_i1;
            i32_store(&instance->w2c_memory, (u64)(var_i0) + 256, var_i1);
            var_i0 = var_l8;
            var_i1 = 4160749567u;
            if (var_i0 > var_i1)
            {
                continue;
            }
            var_i0 = var_l5;
            var_i1 = 32u;
            var_i0 += var_i1;
            var_i1 = var_l8;
            var_i2 = 26u;
            var_i1 >>= (var_i2 & 31);
            var_i2 = 1048768u;
            var_i1 += var_i2;
            var_i1 = i32_load8_u(&instance->w2c_memory, (u64)(var_i1));
            w2c_main_f266(instance, var_i0, var_i1);
            var_i0 = var_l6;
            var_i1 = 4294967295u;
            var_i0 += var_i1;
            var_l6 = var_i0;
        }
    }
    var_i0 = var_l5;
    var_i1 = var_p2;
    var_i2 = 0u;
    var_i3 = var_p1;
    var_i1 = var_i3 ? var_i1 : var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 148, var_i1);
    var_i0 = var_l5;
    var_i1 = var_p1;
    var_i2 = 1049312u;
    var_i3 = var_p1;
    var_i1 = var_i3 ? var_i1 : var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 144, var_i1);
    var_i0 = var_l5;
    var_i1 = 108u;
    var_i0 += var_i1;
    var_i1 = 10u;
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_l5;
    var_i1 = 100u;
    var_i0 += var_i1;
    var_i1 = 11u;
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_l5;
    var_i1 = 92u;
    var_i0 += var_i1;
    var_i1 = 11u;
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_l5;
    var_i1 = 84u;
    var_i0 += var_i1;
    var_i1 = 10u;
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_l5;
    var_i1 = 76u;
    var_i0 += var_i1;
    var_i1 = 13u;
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_l5;
    var_i1 = 11u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 68, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 32u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 104, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 56u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 96, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 144u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 88, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 128u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 80, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 52u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 72, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 24u;
    var_i1 += var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 64, var_i1);
    var_i0 = var_l5;
    var_i1 = 6u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 172, var_i1);
    var_i0 = var_l5;
    var_i1 = 6u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 164, var_i1);
    var_i0 = var_l5;
    var_i1 = 1055600u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 160, var_i1);
    var_i0 = var_l5;
    var_i1 = 0u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 152, var_i1);
    var_i0 = var_l5;
    var_i1 = var_l5;
    var_i2 = 4294967232u;
    var_i1 -= var_i2;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 168, var_i1);
    var_i0 = var_l5;
    var_i1 = 112u;
    var_i0 += var_i1;
    var_i1 = var_l5;
    var_i2 = 152u;
    var_i1 += var_i2;
    w2c_main_f205(instance, var_i0, var_i1); // store char into mem
    var_i0 = var_p0;
    var_i1 = 20u;
    var_i0 += var_i1;
    var_i1 = var_l5;
    var_i2 = 120u;
    var_i1 += var_i2;
    var_i1 = i32_load(&instance->w2c_memory, (u64)(var_i1));
    i32_store(&instance->w2c_memory, (u64)(var_i0), var_i1);
    var_i0 = var_p0;
    var_i1 = var_l5;
    var_j1 = i64_load(&instance->w2c_memory, (u64)(var_i1) + 112u);
    i64_store(&instance->w2c_memory, (u64)(var_i0) + 12, var_j1);
    var_i0 = var_p0;
    var_i1 = 1000000002u;
    i32_store(&instance->w2c_memory, (u64)(var_i0) + 8, var_i1);
    var_i0 = var_l5;
    var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0) + 32u);
    if (var_i0)
    {
        var_i0 = var_l5;
        var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0) + 36u);
        w2c_main_f142(instance, var_i0);
    }
    var_i0 = var_l5;
    var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0) + 128u);
    if (var_i0)
    {
        var_i0 = var_l5;
        var_i0 = i32_load(&instance->w2c_memory, (u64)(var_i0) + 132u);
        w2c_main_f142(instance, var_i0);
    }
    var_i0 = var_l5;
    var_i1 = 176u;
    var_i0 += var_i1;
    instance->w2c_g0 = var_i0;
    FUNC_EPILOGUE;
}
