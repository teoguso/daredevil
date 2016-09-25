using UnityEngine;
using System.Collections;
using System.Collections.Generic;

using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Net.NetworkInformation;

public class UdpState  {
    public IPEndPoint e;
    public UdpClient u;
}


public class SceneController : MonoBehaviour {

    IPEndPoint ip;
    UdpClient listener;
    int test;
    UdpState result_state;
    int gotvalue;
    Byte[] bytesresult;
    IPAddress wifi_ipv4;
    [SerializeField] private GameObject echoobjectPrefab;
    List<GameObject> TheCubes;


	// Use this for initialization
	void Start () {
        result_state = new UdpState();

        gotvalue = 0;

        ip  = new IPEndPoint(IPAddress.Parse("172.26.2.132"), 9939);
        int run = 1;

        listener = new UdpClient(ip);
        TheCubes = new List<GameObject>();

        for (int i = 0; i < 10; i++) {
            GameObject cube;
            cube = Instantiate(echoobjectPrefab) as GameObject;
            TheCubes.Add(cube);
        }

        listener.BeginReceive(receiveCallback, listener);
	}

	// Update is called once per frame
	void Update () {

        if (gotvalue == 1) {

            int i = 0;
            float x = 0.0f;
            float y = 0.0f;
            float z = 0.0f;

            //foreach (GameObject cube in TheCubes) {
            //    Array.Reverse(bytesresult, (i * 12), 4);
            //    Array.Reverse(bytesresult, (i * 12) + 4, 4);
            //    Array.Reverse(bytesresult, (i * 12) + 8, 4);
            //    i++;
            //}
            i = 0;
            foreach (GameObject cube in TheCubes) {
                x = (float)System.BitConverter.ToSingle(bytesresult, 0 + (i * 12)) * 10.0f;
                y = (float)System.BitConverter.ToSingle(bytesresult, 4 + (i * 12)) * 10.0f;
                z = (float)System.BitConverter.ToSingle(bytesresult, 8 + (i * 12)) * 10.0f;
                cube.transform.position = new Vector3(x, y, z);
                i++;
            }
            if (i > 0) {
                Debug.Log("x " + x + " y " + y);
            }
            gotvalue = 0;
            listener.BeginReceive(receiveCallback, listener);
        }
	}

	void receiveCallback(IAsyncResult ar) {
        UdpClient u = (UdpClient)ar.AsyncState;
        IPEndPoint e = new IPEndPoint(IPAddress.Any, 162);
        bytesresult = u.EndReceive(ar, ref e);
        Debug.Log("Got: " + bytesresult.ToString());
        gotvalue = 1;

	}
}
