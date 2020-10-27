using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bomba : MonoBehaviour
{

    private Rigidbody2D rb2d;

    [SerializeField]
    private float velocidade;

    // Start is called before the first frame update
    void Start()
    {
        Movimentar();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void Movimentar()
    {
        rb2d = GetComponent<Rigidbody2D>();
        rb2d.velocity = transform.right * velocidade;
    }
}
