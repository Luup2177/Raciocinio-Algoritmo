def processar_dados(*args, **kwargs):
    print("=== Processando dados ===")
    print(f"\n📦 Args recebidos ({len(args)}):")
    for i, valor in enumerate(args):
        print(f"  [{i}] {valor}")
        print(f"\n🔑 Kwargs recebidos ({len(kwargs)}):")
    for chave, valor in kwargs.items():
        print(f"  {chave} = {valor}")
    resultado = {
        "total_args"  : len(args),
        "total_kwargs": len(kwargs),
        "soma_args"   : sum(x for x in args if isinstance(x, (int, float))),
        "chaves"      : list(kwargs.keys())
    }
    print(f"\n✅ Resumo: {resultado}")
    return resultado


processar_dados(1,5,7,8,9,31 , nome= 'Luigi' , idade=18 , cidade='curitiba')